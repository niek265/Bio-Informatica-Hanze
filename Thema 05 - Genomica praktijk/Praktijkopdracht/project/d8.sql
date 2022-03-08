drop table if exists variants, genes, chromosomes;

create table chromosomes
(   chromosome_id    int             not null,
    chromosome       varchar(15)     not null,
    primary key(chromosome_id)
);

create table genes
(   gene_id         int             not null,
    RefSeq_Gene       varchar(10)     not null,
    chromosome_id	int             not null,
    primary key(gene_id),
    foreign key(chromosome_id)
	    references chromosomes(chromosome_id)
);

create table variants
(   variant_id        int            not null,
    gene_id           int            not null,
    reference         char(1)        not null,
    observed          char(1)        not null,
    POS               int            not null,
    QUAL              char(1)        not null,
    RefSeq_Func       varchar(15),
    dbsnp138          varchar(15),
    1000g2015aug_EUR  float,
    LJB2_SIFT         float,
    LJB2_PolyPhen2_HVAR    varchar(15),
    LJB2_PolyPhen2_HDIV    varchar(15),
    CLINVAR           varchar(30),
    primary key(variant_id),
    foreign key (gene_id)
        references genes(gene_id)
);
