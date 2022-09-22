package section2_syntax.part1_datatypes;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Creation date: May 28, 2018
 *
 * @author Michiel Noback (&copy; 2018)
 * @version 0.01
 */
class DatatypesTest {
    private static final double DELTA = 1e-10;
    private Datatypes datatypes;

    @BeforeEach
    void setup() {
        this.datatypes = new Datatypes();
    }

    @Test
    void correctDataType0() {
        assertEquals("short", datatypes.correctDataType0(), "don't use more precision than needed");
    }

    @Test
    void correctDataType1() {
        assertEquals("long", datatypes.correctDataType1(), "this obviously does not fit in an int");
    }

    @Test
    void correctDataType2() {
        assertEquals("float", datatypes.correctDataType2(), "did you use double? a bit too precise ");
    }

    @Test
    void correctDataType3() {
        assertEquals("float", datatypes.correctDataType3(), "did you use double? a bit too precise ");
    }

    @Test
    void correctDataType4() {
        assertEquals("boolean", datatypes.correctDataType4(), "life and death only know two states...");
    }

    @Test
    void correctDataType5() {
        assertEquals("String", datatypes.correctDataType5(), "duh");
    }

    @Test
    void correctDataType6() {
        assertEquals("char", datatypes.correctDataType6(), "Three genders can be specified by single letters...");
    }

    @Test
    void determineGCfraction() {
        assertEquals(0.5, datatypes.determineGCfraction("AAGGCCTT"), DELTA, "Did you convert the count to the right type");
        assertEquals(0.5, datatypes.determineGCfraction("aaggcctt"), DELTA, "Did you convert the DNA to upper case?");
        assertEquals(0, datatypes.determineGCfraction("AAAAAAAA"), DELTA);
    }

    @Test
    void modifyString() {
        String result = datatypes.modifyString();
        assertEquals("where can I find the sodamachine in this building?", result);
    }

    @Test
    void getFirstAndLast() {
        Integer[] input = new Integer[4];
        input[0] = 42;
        input[3] = 24;
        String[] expected = new String[]{"42", "24"};
        String[] actual = datatypes.getFirstAndLastAsStringRepresentation(input);

        assertArrayEquals(expected, actual);

        Double[] input2 = new Double[3];
        input2[0] = 2.71;
        input2[2] = 3.14;
        expected = new String[]{"2.71", "3.14"};
        actual = datatypes.getFirstAndLastAsStringRepresentation(input2);

        assertArrayEquals(expected, actual);
    }

    @Test
    void cubeAll1() {
        int[] input = {0, 1, 2, 3};
        int[] expected = {0, 1, 8, 27};
        int[] observed = datatypes.cubeAll(input);

        assertArrayEquals(expected, observed);
    }

    @Test
    void cubeAll2() {
        int[] input = {2, 3, 5};
        int[] expected = {8, 27, 125};
        int[] observed = datatypes.cubeAll(input);

        assertArrayEquals(expected, observed);
    }

    @Test
    void cumulativeProduct() {
        int[] input = {0, 1, 2, 3};
        assertThat(datatypes.cumulativeProduct(input)).isEqualTo(0);

        input = new int[]{2, 3, 5};
        assertThat(datatypes.cumulativeProduct(input)).isEqualTo(30);
    }
}