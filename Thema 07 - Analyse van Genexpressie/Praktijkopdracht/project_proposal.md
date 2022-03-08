# Project Proposal
_Niek Scholten  
388602_

Dit project gaat over het effect van door prionen veroorzaakte neurotoxiciteit op de genactiviteit.  
Specifiek op Drosophila Melanogaster in dit geval.  

De Drosophila zijn in het larve stadium blootgesteld aan hersenweefsel van schapen,  
de ene populatie werd blootgesteld aan weefsel van schapen die Scrapie hadden, en de andere aan weefsel van schapen die geen Scrapie hadden.  
Bij het uitgroeien van de larve tot een vlieg, werden ze gehouden in buisjes.  
Na 5, 30 of 40 dagen werden ze geëuthanaseerd en onthoofd voor RNA-extractie.  

De data duidt erop dat afwijkende cell cyclus activiteit, onderdrukking van eiwit synthese en aangepaste mitochondriale functies een belangrijke rol spelen in door prionen veroorzaakte neurotoxiciteit.  
En deze bevindingen komen overeen met bevindingen in zoogdieren.

De data is verdeeld in 12 groepen en volgt de volgende benaming:  

FlyLine_Age_Treatment_Replicant

Fly lines:
* Elav x 51D
* Elav x PrP (Cyt)
* Elav x PrP (GPI)

Age in days:
* 5
* 30
* 40

Treatment:
* Normal Brain Homogenate (NBH)
* Scrapie (S)

Elke groep heeft 3 replicaten.  

Dit is de beschrijving van de processing voor de data:  
Fastq reads were mapped to Drosophila Genome (built BDGP6) using Tophat V2.0.11  
htseq-count 0.6.1p1 was used to generate gene level counts based on Ensembl V77 GTF  
Differential gene expression was performed using edgeR  
Genome_build: BDGP6  
Supplementary_files_format_and_content: tab-delimited text containing raw gene-level count for each sample

Voorbeeld van de data:  
```
FBgn0000003	0
FBgn0000008	744
FBgn0000014	1
FBgn0000015	0
FBgn0000017	1019
```

Het idee achter dit project is om de data met elkaar te vergelijken en de conclusie van de onderzoekers te bevestigen.  
