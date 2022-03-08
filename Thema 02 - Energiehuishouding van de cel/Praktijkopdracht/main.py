#!/usr/bin/env python3

"""
Animeert het translatie proces van mRNA
"""

__author__ = 'Gijs Bakker, Niek Scholten'

import sys
from math import pi
import nonpov
import bintemplate
from pypovray import pypovray, SETTINGS, pdb
from vapory import Scene, Camera, LightSource


nucleomoddel_list = []
triplet_list = []
key_cycle = 0
aminomoddel_list = []
AMINO_AFSTAND = 41
key = pdb.PDBMolecule('{}/pdbeind/tRNA.pdb'.format(SETTINGS.AppLocation), center=True)


def nucleo_maker(nucleo_str):
    """Voegt voor elke nucleotide in de nucleotide string een 3d structuur en voegt deze
    aan een list toe.
    Args: nucleo_str: een string van nucleotiden"""
    global nucleomoddel_list
    naam = ""
    for nucleotide in nucleo_str:
        if nucleotide == 'A':
            naam = '{}/pdbeind/Adenine.pdb'
        elif nucleotide == 'U':
            naam = '{}/pdbeind/Uracil.pdb'
        elif nucleotide == 'C':
            naam = '{}/pdbeind/Guanine.pdb'
        elif nucleotide == 'G':
            naam = '{}/pdbeind/Thymine.pdb'
        nucleomoddel_list.append(pdb.PDBMolecule(naam.format(SETTINGS.AppLocation),
                                                 center=True))


def amino_lister(tripletten):
    """Voegt de 3d structuur van elk aminozuur in de tripletten lijst
    toe aan een globale list.
    Args: tripletten: Een list die strings van tripletten bevat."""
    global aminomoddel_list
    for triplet in tripletten:
        aminomoddel_list.append(amino_maker(triplet))


def amino_maker(triplet):
    """Genereerd een aminozuur bij een triplet.
    args: triplet: Het triplet waar het aminozuur bij ge genereerd moet worden.
    return: De PDBMolecule van het aminozuur"""

    locatie = '{a}/pdbeind/{b}.pdb'
    aminozuur = bintemplate.TRIPLETTOAMINO[triplet]
    amino = pdb.PDBMolecule(locatie.format(a=SETTINGS.AppLocation, b=aminozuur), center=True)
    return amino


def key_maker():
    """Zet de 3d structuur van de key in de juiste rotatie."""
    global key
    key.rotate([0, 1, 0], 0.5)
    key.rotate([1, 0, 0], 2*pi)
    key.rotate([0, 0, 1], pi-0.6)


def move_nucleotides(step, cycle, key_nmbr, bewegend=True, afstand=7):
    """Verplaatst de nucleotiden aan de hand van hoelang 1 cyclus van de
    key duurt en welke cyclus momenteel bezig is.
    Args: step: het nummer van het frame. cycle: het aantal frames dat de key er over
    doet om over het scherm te verplaatsen. key_nmbr: het nummer van de key cyclus.
    bewegend: een boolian die aangeeft of de nucleotiden moeten bewegen.
    afstand: de afstand die tussen de nucleotiden moet zitten."""
    x_pos = -17     # de x positie van de eerste nucleotide.
    # De 1e step in de 2e helft van de cyclus als step 1 zetten
    step2 = step - (cycle*key_nmbr) - (cycle/2)
    afs_per_step = afstand / (cycle / 2) * step2 * 3    # *3 omdat het een triplet moet opschuiven.
    afs = afstand * key_nmbr * 3
    if not bewegend:
        afs_per_step = 0

    for element in nucleomoddel_list:
        element.move_to([x_pos - afs_per_step - afs, -42, -10])
        x_pos += afstand


def move_aminozuren(step, cycle, key_nmbr, bewegend=True, afstand=7):
    """Verplaatst de aminozuren aan de hand van hoelang 1 cyclus van de
    key duurt en welke cyclus momenteel bezig is.
    Args: step: het nummer van het frame. cycle: het aantal frames dat de key er over
    doet om over het scherm te verplaatsen. key_nmbr: het nummer van de key cyclus.
    bewegend: een boolian die aangeeft of de nucleotiden moeten bewegen.
    afstand: de afstand die tussen de nucleotiden moet zitten."""
    x_pos = 0
    # De 1e step in de 2e helft van de cyclus als step 1 zetten
    step2 = step - (cycle*key_nmbr) - (cycle/2)
    # Berekent de afstand die per step afgelecht moet worden
    afs_per_step = afstand / (cycle / 2) * step2
    afs = afstand * key_nmbr
    if not bewegend:
        afs_per_step = 0

    for element in aminomoddel_list:
        element.move_to([x_pos - afs_per_step - afs, AMINO_AFSTAND, 0])
        x_pos += afstand


def frame(step):
    """Berekeent de posities van alle elementen van de animatie. En simuleert de animatie.
    Args: step: het nummer van het frame.
    Return: een Scene"""
    global aminomoddel_list

    # juiste triplet pakken key en aminozuur bij maken en key verplaatsen
    key_nmbr = step // key_cycle  # key_nmbr = het nummer van de momentele key cyclus
    triplet = triplet_list[key_nmbr]  # welk triplet de key moet mee nemen
    amino = amino_maker(triplet)

    pos = move_key(step, key_cycle, key)
    amino.move_to([pos[0], pos[1] + AMINO_AFSTAND, pos[2]])

    camera = Camera('location', [0, 8, -140], 'look_at', [0, 0, 0])
    light = LightSource([0, 40, -100], 2)
    objects = [light]
    move_aminozuren(step, key_cycle, key_nmbr, False)   # zet de aminozuren op de juiste positie
    move_nucleotides(step, key_cycle, key_nmbr, False)  # zet de nucleotide op de juiste positie

    if pos[0] > 0:
        if key_nmbr > 0:
            # voegt alle amino modellen toe uit de aminomoddel_list
            # tot aan het molecuul wat de key momenteel mee neemt
            for i in range(key_nmbr):
                objects += aminomoddel_list[i].povray_molecule
        objects += key.povray_molecule + amino.povray_molecule

    elif pos[0] == 0:
        # voegt alle amino modellen toe uit de aminomoddel_list
        # tot en met aan het molecuul wat de key momenteel mee neemt
        for i in range(key_nmbr+1):
            objects += aminomoddel_list[i].povray_molecule
        objects += key.povray_molecule

    elif pos[0] < 0:
        # voegt alle amino modellen toe uit de aminomoddel_list
        # tot en met aan het molecuul wat de key momenteel mee neemt
        # en verplaatst de nucleotiden en aminozuren
        move_aminozuren(step, key_cycle, key_nmbr)
        move_nucleotides(step, key_cycle, key_nmbr)
        for i in range(key_nmbr+1):
            objects += aminomoddel_list[i].povray_molecule
        objects += key.povray_molecule

    for element in nucleomoddel_list:
        objects += element.povray_molecule

    return Scene(camera, objects)


def move_key(step, nsteps, key_moddel, start_pos=(150, 50, 0),
             eind_pos=(-200, 50, 50), mid_pos=(0, 0, 0)):
    """Laat de key van rechts boven naar midden onder naar links boven bewegen.
    args: step: welke frame het programma bezig is.
    nsteps: totaal aantal steps dat het duurt om van de beweging te maken.
    key: Het PDBMolecule dat verplaatst moet worden
    return: De positie van de center van de key"""

    cycle_step = step % (nsteps/2)
    if step % nsteps < nsteps / 2:
        # de volgende positie die in de cyclus aan genomen moet worden
        pos_now = [start_pos[0] + (mid_pos[0] - start_pos[0]) / (nsteps / 2) * cycle_step,
                   start_pos[1] + (mid_pos[1] - start_pos[1]) / (nsteps / 2) * cycle_step,
                   start_pos[2] + (mid_pos[2] - start_pos[2]) / (nsteps / 2) * cycle_step]
    else:
        pos_now = [mid_pos[0] + (eind_pos[0] - mid_pos[0]) / (nsteps / 2) * cycle_step,
                   mid_pos[1] + (eind_pos[1] - mid_pos[1]) / (nsteps / 2) * cycle_step,
                   mid_pos[2] + (eind_pos[2] - mid_pos[2]) / (nsteps / 2) * cycle_step]

    key_moddel.move_to(pos_now)
    return key_moddel.center


def main(args):
    """Maakt een animatie van het translatie proces van mRNA aan de hand van de input.
    args: 2e argument is de filenaam, 3e argument is hoeveel fps de video gerenderd moet worden,
    wordt er niets ingevuld dan wordt de fps uit default.ini gehaalt.
    4e argument hoeveel tripletten er vertaalt moeten worden in de animatie."""
    global triplet_list, key_cycle

    # user data gebruiken
    if len(args) >= 2:
        file_naam = args[1]  # de mRNA sequencie die getransleert moet worden
    else:
        print("You did not gave a file name")
        return 0
    if len(args) >= 3 and args[2].isdigit():
        fps = int(args[2])     # fps
    else:
        fps = int(SETTINGS.RenderFPS)

    # verwerken
    mrna = nonpov.read_fasta(file_naam)
    triplet_list = nonpov.triplet_maker(mrna)
    nucleo_maker(mrna)
    amino_lister(triplet_list)
    key_maker()

    # lengte filmpje en key cycle instellen
    SETTINGS.RenderFPS = fps
    key_cycle = fps*2
    if len(args) >= 4 and args[3].isdigit() and int(args[3] <= len(triplet_list)):
        SETTINGS.NumberFrames = str(int(args[3]) * key_cycle)   #De lengte van de video berekenen
    else:
        SETTINGS.NumberFrames = str(len(triplet_list) * key_cycle)

    pypovray.render_scene_to_mp4(frame)
    return 0


if __name__ == "__main__":
    exitcode = main(sys.argv)
    sys.exit(exitcode)
