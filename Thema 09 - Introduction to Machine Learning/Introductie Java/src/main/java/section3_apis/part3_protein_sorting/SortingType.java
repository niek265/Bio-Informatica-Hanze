/*
 * Copyright (c) 2015 Michiel Noback [michiel.noback@gmail.com].
 * All rights reserved.
 */
package section3_apis.part3_protein_sorting;

/**
 *
 * @author Michiel Noback [michiel.noback@gmail.com]
 */
public enum SortingType {
    PROTEIN_NAME("simple namesort"),
    ACCESSION_NUMBER("accession number sort"),
    GO_ANNOTATION("GO annotation"),
    PROTEIN_WEIGHT("protein molecular weight");
    
    private String type;
    
    private SortingType(String type) {
        this.type = type;
    }

    @Override
    public String toString() {
        return "SortingType{" + "type=" + type + '}';
    }
}
