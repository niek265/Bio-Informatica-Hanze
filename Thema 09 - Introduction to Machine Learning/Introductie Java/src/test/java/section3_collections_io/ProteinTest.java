package section3_collections_io;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import section3_apis.part3_protein_sorting.*;

import java.util.Collections;
import java.util.Comparator;
import java.util.List;

import static org.assertj.core.api.AssertionsForInterfaceTypes.assertThat;
import static org.junit.jupiter.api.Assertions.*;

class ProteinTest {
    private List<Protein> proteins = null;

    @BeforeEach
    void setup() {
        ProteinDataSource dataSource = new ProteinDataSourceInMemory();
        this.proteins = dataSource.getAllProteins();
    }

    @Nested
    @DisplayName("Tests natural ordering on protein name")
    class NaturalOrdering {
        //YOU CAN RUN ALL THESE TESTS AT ONCE
        @Test
        @DisplayName("Test A: less than")
        public void testCompareTo_A() {
            Protein o = new Protein("mannosidase alpha", "man1b1a", "MRTVALL", null);
            Protein instance = new Protein("60s ribosomal protein l35 pthr13872", "Stt3a", "MTDDLVLAW", null);
            int result = instance.compareTo(o);
            assertTrue(result < 0);
        }
        @Test
        @DisplayName("Test B: greater than")
        public void testCompareTo_B() {
            Protein instance = new Protein("mannosidase alpha", "man1b1a", "MRTVALL", null);
            Protein o = new Protein("60s ribosomal protein l35 pthr13872", "Stt3a", "MTDDLVLAW", null);
            int result = instance.compareTo(o);
            assertTrue(result > 0);
        }
        @Test
        @DisplayName("Test C: equal")
        public void testCompareTo_C() {
            Protein o = new Protein("mannosidase alpha", "man1b1a", "MRTVALL", null);
            Protein instance = new Protein("mannosidase alpha", "Stt3a", "MTDDLVLAW", null);
            int expResult = 0;
            int result = instance.compareTo(o);
            assertEquals(expResult, result);
        }
    }

    @Nested
    @DisplayName("Tests different Comparators for protein sorting")
    class ComparatorFactory {
        @Test
        @DisplayName("Tests the IllegalArgument handling")
        public void testGetSorter_A() {
            SortingType type = null;
            try {
                Protein.getSorter(type);
                fail(String.format("Testing fetching sorter with type %s ... expected %s", type, IllegalArgumentException.class.getName()));
            } catch (IllegalArgumentException ex) {
                assertTrue(true);
            }
        }

        @Test
        @DisplayName("Tests Comparator on protein name")
        public void testGetSorter_B() {
            SortingType type = SortingType.PROTEIN_NAME;
            Comparator<Protein> comparator = Protein.getSorter(type);
            Protein one = new Protein("mannosidase alpha", "man1b1a", "MRTVALL", null);

            Protein two = new Protein("60s ribosomal protein l35 pthr13872", "Stt3a", "MTDDLVLAW", null);
            assertThat(comparator.compare(one, two)).isGreaterThan(0);

            two = new Protein("Ribosomal protein l35 pthr13872", "Stt3a", "MTDDLVLAW", null);
            assertThat(comparator.compare(one, two)).isGreaterThan(0);

            two = new Protein("mannosidase alpha", "Stt3a", "MTDDLVLAW", null);
            assertThat(comparator.compare(one, two)).isEqualTo(0);
        }

        @Test
        @DisplayName("Tests Comparator for Accession number")
        public void testGetSorter_C() {
            SortingType type = SortingType.ACCESSION_NUMBER;
            Comparator<Protein> comparator = Protein.getSorter(type);
            String[] expAccnos = new String[]{
                    "Fut8",
                    "man1b1a",
                    "Stt3a",
                    "Syvn1",
                    "Tusc3"};
            //sort the list
            Collections.sort(proteins, comparator);
            checkOrderOfAccessionNumbers(type, expAccnos);
        }

        @Test
        @DisplayName("Tests Comparator of protein weight")
        public void testGetSorter_D() {
            SortingType type = SortingType.PROTEIN_WEIGHT;
            Comparator<Protein> comparator = Protein.getSorter(type);

            Protein one = new Protein("mannosidase alpha", "man1b1a", "MRTVALL", null);

            Protein two = new Protein("60s ribosomal protein l35 pthr13872", "Stt3a", "MTDDLVLAW", null);
            assertThat(comparator.compare(one, two)).isLessThan(0);

            two = new Protein("Ribosomal protein l35 pthr13872", "Stt3a", "MTDD", null);
            assertThat(comparator.compare(one, two)).isGreaterThan(0);

            two = new Protein("mannosidase alpha", "Stt3a", "MRTVALL", null);
            assertThat(comparator.compare(one, two)).isEqualTo(0);
        }

        @Test
        @DisplayName("Tests Comparator of GO annotation")
        public void testGetSorter_E() {
            SortingType type = SortingType.GO_ANNOTATION;
            //first on biological process (3), then on cellular component (1) and last on molecular function (2)
            Comparator<Protein> comparator = Protein.getSorter(type);

            Protein one = new Protein("mannosidase alpha", "man1b1a", "MRTVALL",
                    new GOannotation(13259,
                            "cytoplasmatic",
                            "synoviolin-related",
                            "cell-cycle regulation"));

            //primary on biological process, secondary on cellular component and lastly on molecular
            //function
            Protein two = new Protein("60s ribosomal protein l35 pthr13872", "Stt3a", "MTDDLVLAW",
                    new GOannotation(18269,
                            "mitochondrial",
                            "dolichyl-diphosphooligosaccharide--protein glycosyltransferase",
                            "sugar metabolism"));

            assertThat(comparator.compare(one, two)).isLessThan(0);

            two = new Protein("Ribosomal protein l35 pthr13872", "Stt3a", "MTDD",
                    new GOannotation(12345,
                            "mitochondrial",
                            "dolichyl-diphosphooligosaccharide--protein glycosyltransferase",
                            "cell-cycle regulation"));

            assertThat(comparator.compare(one, two)).isLessThan(0);

            two = new Protein("mannosidase alpha", "Stt3a", "MRTVALL",
                    new GOannotation(34221,
                            "cytoplasmatic",
                            "dolichyl-diphosphooligosaccharide--protein glycosyltransferase",
                            "cell-cycle regulation"));

            assertThat(comparator.compare(one, two)).isGreaterThan(0);

            two = new Protein("mannosidase alpha", "Stt3a", "MRTVALL",
                    new GOannotation(45336,
                            "cytoplasmatic",
                            "synoviolin-related",
                            "cell-cycle regulation"));

            assertThat(comparator.compare(one, two)).isEqualTo(0);
        }
    }

    /**
     * Utility method.
     * @param type
     * @param expAccnos
     */
    private void checkOrderOfAccessionNumbers(SortingType type, String[] expAccnos) {
        for (int i = 0; i < expAccnos.length; i++) {
            String expAccno = expAccnos[i];
            String obsAccno = this.proteins.get(i).getAccession();
            //System.out.println("comparing obsName = " + obsName + " with expName = " + expName);
            if (!expAccno.equals(obsAccno)) {
                fail(String.format("Testing sorting with \"%s\" failed", type.name()));
            }
        }
    }
}