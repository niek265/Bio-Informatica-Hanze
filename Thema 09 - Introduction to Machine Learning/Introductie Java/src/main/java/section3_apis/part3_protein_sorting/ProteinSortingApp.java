/*
 * Copyright (c) 2015 Michiel Noback [michiel.noback@gmail.com].
 * All rights reserved.
 */

package section3_apis.part3_protein_sorting;

import java.util.Collections;
import java.util.List;

/**
 *
 * @author Michiel Noback [michiel.noback@gmail.com]
 * @version 0.0.1
 */
public class ProteinSortingApp {
    /**
     * main method solely for testing purposes
     * @param args the CL args
     */
    public static void main(String[] args) {
        ProteinDataSource proteinDataSource = new ProteinDataSourceInMemory();
        List<Protein> proteins = proteinDataSource.getAllProteins();

        Collections.sort(proteins, Protein.getSorter(SortingType.PROTEIN_WEIGHT));
        
        proteins.stream().forEach(System.out::println);
    }
}
