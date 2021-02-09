--1a
select x_coord from cells  where id=14;
--1b
select g.id from gene_expressions g, cells c where g.cell = c.id and cell_type = ĺiver; 
--1c
select g.id from gene_expressions g join cells c on g.cell = c.id where cell_type = ĺiver; 
-- 1d
select max(id) from genes;
--1e
select cell_type from cells c join gene_expressions ge on ge.cell = c where expression_value = (select min(expression_value) from gene_expressions);
--1f
select gene_symbol from genes g join gene_expressions ge on g.id = ge.gene join cells c on c.id = ge.cell where cell_type is null order by gene_symbol;
--1g
select gene_symbol from genes g join gene_expressions ge on g.id = ge.gene join cells c on c.id = ge.cell where cell_type is ´liver´i order by gene_symbol desc;
--1h
select gene_symbol, avg(expression_value) from genes g join gene_expressions ge on g.id = ge.gene where cell_type = ´blood´ and stimulated = 1 group by gene_symbol order by avg(expression_value) desc;

--2a
update genes_expressions set gene = (select id from genes where gene_symbol = '>gi|124505651 MAL1P4.04');
delete from genes where gene_symbol = '>gi|124505651 MAL1P4.06b'; 
--2b
alter table cells drop column sample;
--2c
alter table genes modify gene_symbol varchar(255) not null default ´N.N.´;

Normering:
Vraag 1: query direct uitvoerbaar (copy-paste in de mysql client) 5 pnt, als niet uitvoerbaar door het vergeten van quotes of ; dan 2 pnt.
overtollige subqueries etc: 0 pnt
where ipv join: 0 pnt
Vraag 1 h: als niet uitvoerbaar maar bevat wel group by dan 3 punten
als fout gesorteerd max 2 pnt
aals fout veld: max 2 pnt
meer dan 1 fout: 0 pnt

Vraag 2: queries direct uitvoerbaar (copy-paste in de mysql client)
    gebruik subquery 5 pnt (dus zonder: 5 pnt aftrek)
