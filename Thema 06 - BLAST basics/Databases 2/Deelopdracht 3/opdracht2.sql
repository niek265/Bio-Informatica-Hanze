DROP TABLE IF EXISTS /* If the tables exist, drop them and recreate them */
    microarray,
    probe,
    oligonucleotide,
    identifier,
    gene,
    chromosome,
    organism;

CREATE TABLE organism /* Full taxonomy of an organism */
(   organism_id         INTEGER     NOT NULL AUTO_INCREMENT,
    species             TEXT    NOT NULL, /* Only species and genus are required */
    genus               TEXT    NOT NULL,
    family              TEXT,
    `order`             TEXT,
    class               TEXT,
    phylum              TEXT,
    kingdom             TEXT,
    domain              TEXT,
    PRIMARY KEY(organism_id) /* Primary keys are id's so the lookup speed is higher */
);

CREATE TABLE chromosome
(   chromosome_id       INTEGER         NOT NULL AUTO_INCREMENT,
    chromosome          TEXT            NOT NULL,
    organism_id         INTEGER         NOT NULL,
    PRIMARY KEY(chromosome_id),
    FOREIGN KEY(organism_id)
        REFERENCES organism(organism_id)
);

CREATE TABLE gene
(   gene_id             INTEGER         NOT NULL AUTO_INCREMENT,
    seq                 LONGTEXT        NOT NULL, /* LONGTEXT has a maximum of 4294967295 characters, might the sequence be this long */
    chromosome_id       INTEGER         NOT NULL,
    PRIMARY KEY(gene_id),
    FOREIGN KEY(chromosome_id)
        REFERENCES chromosome(chromosome_id)
);

CREATE TABLE identifier
(   identifier_id       INTEGER         NOT NULL AUTO_INCREMENT,
    name                VARCHAR(255)    NOT NULL,
    gene_id             INTEGER         NOT NULL,
    PRIMARY KEY(identifier_id),
    FOREIGN KEY(gene_id)
        REFERENCES genes(gene_id)
);

CREATE TABLE oligonucleotide
(   oligo_id            INTEGER         NOT NULL AUTO_INCREMENT,
    gc                  FLOAT           NOT NULL, /* Floats are used to store decimal values */
    melt_temp           FLOAT           NOT NULL,
    `unique`            BOOLEAN         NOT NULL,
    repeats             BOOLEAN         NOT NULL,
    hairpins            BOOLEAN         NOT NULL,
    gene_id             INTEGER         NOT NULL,
    PRIMARY KEY(oligo_id),
    FOREIGN KEY(gene_id)    REFERENCES genes(gene_id)
);

CREATE TABLE microarray
(   array_id            INTEGER         NOT NULL AUTO_INCREMENT,
    quality             FLOAT           NOT NULL,
    incubation_temp     FLOAT           NOT NULL,
    PRIMARY KEY(array_id)
);

CREATE TABLE probe /* Acts as an extra layer between oligonucleotide and microarray */
(   probe_id            INTEGER         NOT NULL AUTO_INCREMENT,
    oligo_id            INTEGER         NOT NULL,
    array_id            INTEGER         NOT NULL,
    PRIMARY KEY(probe_id),
    FOREIGN KEY(oligo_id)
        REFERENCES oligonucleotide(oligo_id),
    FOREIGN KEY(array_id)
        REFERENCES microarray(array_id)
);