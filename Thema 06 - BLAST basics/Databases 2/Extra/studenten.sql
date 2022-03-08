-- verwijder de tabellen voordat je ze aanmaakt, anders krijg je een error
drop table if exists examens; -- sluit al je opdrachten af met een ;
drop table if exists studenten;
drop table if exists cursussen;

/* maak een tabel voor de studenten aan
    zorg er voor dat je elke letter hiervan snapt!!!
    zie de online documentatie of gebruik de help functie van de client.
*/
create table studenten
(   stud_id         char(4)     not null,
    voorletters     varchar(15) not null,
    naam            varchar(15) not null,
    tussenvoegsel   varchar(8),
    woonplaats      varchar(15) not null,
    geb_datum       date,
    mentor          char(4),
    primary key(stud_id)
);

create table cursussen
(   cur_id          char(4)     not null,
    naam            varchar(25) not null,
    primary key(cur_id)
);

/* Deze tabel 'refereert' naar de andere twee tabellen en kan dus pas na die twee aangemaakt worden.
    (anders wordt er een tijdje naar iets niet-bestaands verwezen).
    Bij het verwijderen is om dezelfde reden de volgorde omgekeerd! (Zie boven)
*/
create table examens
(   stud_id         char(4)     not null,
    cur_id          char(4)     not null,
    ex_datum        date,
    cijfer          int(2),
    primary key(stud_id, cur_id),
    foreign key (stud_id)
        references studenten(stud_id)
        on delete restrict,
    foreign key (cur_id)
        references cursussen(cur_id)
            on update cascade
);

-- Zet de inhoud in de tabellen. Ook hierbij is de volgorde soms van belang!
insert into cursussen(cur_id, naam) values('inin', 'inleiding informatica');
insert into cursussen(cur_id, naam) values('dab1', 'databases 1');
insert into cursussen(cur_id, naam) values('dab2', 'databases2');
insert into cursussen(cur_id, naam) values('biol', 'biologie 1');
insert into cursussen(cur_id, naam) values('java', 'progr. in Java');

insert into studenten(stud_id, voorletters, naam, tussenvoegsel, woonplaats, geb_datum, mentor) values('parn', 'am', 'poortinga', null, 'garrelsweer', '1967-02-05', null);
insert into studenten(stud_id, voorletters, naam, tussenvoegsel, woonplaats, geb_datum, mentor) values('bakk', 'ja', 'bakker', null, 'groningen', '1980-08-06', 'parn');
insert into studenten(stud_id, voorletters, naam, tussenvoegsel, woonplaats, geb_datum, mentor) values('cals', 'cm', 'cals', null, 'assen', '1990-12-01', null);
insert into studenten(stud_id, voorletters, naam, tussenvoegsel, woonplaats, geb_datum, mentor) values('nieu', 'a', 'nieuwkerk', null, 'leeuwarden', '1992-02-03', null);
insert into studenten(stud_id, voorletters, naam, tussenvoegsel, woonplaats, geb_datum, mentor) values('worm', 'e', 'worms', null, 'vries', '1991-03-08', 'parn');
insert into studenten(stud_id, voorletters, naam, tussenvoegsel, woonplaats, geb_datum, mentor) values('jans', 'r', 'jansen', null, 'annen', '1989-05-05', 'parn');
insert into studenten(stud_id, voorletters, naam, tussenvoegsel, woonplaats, geb_datum, mentor) values('janw', 'w', 'jansen', null, 'annen', '1990-12-09', 'parn');
insert into studenten(stud_id, voorletters, naam, tussenvoegsel, woonplaats, geb_datum, mentor) values('spaa', 'r', 'spaans', null, 'groningen', '1990-09-13', null);
insert into studenten(stud_id, voorletters, naam, tussenvoegsel, woonplaats, geb_datum, mentor) values('baa', 'k', 'baan', null, 'groningen', '1991-09-14', null);
insert into studenten(stud_id, voorletters, naam, tussenvoegsel, woonplaats, geb_datum, mentor) values('mole', 'e', 'molenbeek', null, 'buitenpost', '1989-11-11', 'parn');
insert into studenten(stud_id, voorletters, naam, tussenvoegsel, woonplaats, geb_datum, mentor) values('myra', 'n', 'myra', 'van', 'barcelona', '250-05-12', null);
insert into studenten(stud_id, voorletters, naam, tussenvoegsel, woonplaats, geb_datum, mentor) values('bikk', 'g', 'bikkel', null, 'appingedam', '1990-03-07', 'parn');
insert into studenten(stud_id, voorletters, naam, tussenvoegsel, woonplaats, geb_datum, mentor) values('hofm', 'pk', 'hofman', null, 'appingedam', '1990-04-07', null);
insert into studenten(stud_id, voorletters, naam, tussenvoegsel, woonplaats, geb_datum, mentor) values('temm', 'd', 'temming', null, 'groningen', '1990-05-07', null);

insert into examens(stud_id, cur_id, ex_datum, cijfer) values('hofm', 'dab2', '05-11-25', 6);
insert into examens(stud_id, cur_id, ex_datum, cijfer) values('spaa', 'biol', '04-05-04', 9);
insert into examens(stud_id, cur_id, ex_datum, cijfer) values('hofm', 'dab1', '30-10-06', 4);
insert into examens(stud_id, cur_id, ex_datum, cijfer) values('nieu', 'inin', '07-09-24', 6);
insert into examens(stud_id, cur_id, ex_datum, cijfer) values('jans', 'dab2', '05-11-25', 7);
insert into examens(stud_id, cur_id, ex_datum, cijfer) values('hofm', 'java', '07-09-25', 3);
insert into examens(stud_id, cur_id, ex_datum, cijfer) values('nieu', 'biol', '02-05-05', 8);
insert into examens(stud_id, cur_id, ex_datum, cijfer) values('jans', 'inin', '03-11-21', 8);
insert into examens(stud_id, cur_id, ex_datum, cijfer) values('nieu', 'dab2', '05-09-11', 7);
insert into examens(stud_id, cur_id, ex_datum, cijfer) values('spaa', 'dab1', '07-10-10', null);
insert into examens(stud_id, cur_id, ex_datum, cijfer) values('mole', 'java', null, null);
