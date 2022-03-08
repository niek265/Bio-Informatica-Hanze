## Auteurs
Gijs Bakker
Niek Scholten

## Datum
16-01-2019

## Files
main.py v3.1
Maakt een animatie van de translatie van het mRNA van het gegeven fasta bestand

nonpov.py v1.1
Bevat de functies voor het inlezen en gebruik maken van het fasta bestand

bintemplate.py v 2.0
Bevat dictionarys voor het vertalen van een triplet naar een aminozuur

pdb files van de aminozuren
    A.pdb
    C.pdb
    D.pdb
    E.pdb
    F.pdb
    G.pdb
    H.pdb
    I.pdb
    K.pdb
    L.pdb
    M.pdb
    N.pdb
    P.pdb
    Q.pdb
    R.pdb
    S.pdb
    T.pdb
    V.pdb
    W.pdb
    Y.pdb
verkregen met:
http://www.cryst.bbk.ac.uk/education/AminoAcid/the_twenty.html 19-12-2018 voor de aminozuur afkortingen
https://files.rcsb.org/ligands/view/VAL_model.sdf voor het sdf bestand
https://cactus.nci.nih.gov/translate/ 19-12-2018 voor het maken van de pdb files

pdb files van de nucleotide
    Adenine.pdb
    Cytosine.pdb
    Guanine.pdb
    Thymine.pdb
    Uracil.pdb
verkregen met:
https://www.rcsb.org

pdb file van tRNA
    tRNA.pdb
verkregen met:
https://www.rcsb.org

## Versie
v3.1

## Doel
Dit programma maakt een animatie van de translatie van mRNA uit een gegeven fasta bestand,
om het translatie proces inzichtelijker te maken.

## Syntax
Om de animatie te renderen dient het programma main.py via de terminal gerunt te worden
$ python3 main.py file-naam fps tripletten

main.py:
    De naam het programma dat geladen moet worden. "main.py"
file-naam:
    De naam van de fasta file waar het filmpje op gebassert wordt
fps:
    Een geheel getal dat het aantal frames per seconden van de animatie.
    Wordt hier niets of het verkeerde ingevult dan wordt het aantal fps uit default.ini gehaalt 
tripletten
    Een geheel getal dat aangeeft hoeveel tripletten vertaalt moeten worden in de animatie
    Wordt hier niets of het verkeerde ingevult dan worden alle tripletten vertaalt
         
Dit programma kan met meerdere workers worden uitgevoert.
