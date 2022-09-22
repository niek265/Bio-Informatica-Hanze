package section2_syntax.part3_flow_control;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.jupiter.api.Assertions.*;

class AllSubstringsPrinterTest {

    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private final AllSubstringsPrinter asp = new AllSubstringsPrinter();

    @Test
    void printSubstringsLeftAlignedLeftTruncatedA() {
        String stringToSubstring = "GATCG";
        String expectedPrint =
                "GATCG" + System.lineSeparator() +
                        "ATCG" + System.lineSeparator() +
                        "TCG" + System.lineSeparator() +
                        "CG" + System.lineSeparator() +
                        "G" + System.lineSeparator();
        asp.printSubstringsLeftAlignedLeftTruncated(stringToSubstring);
        assertEquals(expectedPrint, outContent.toString());
    }

//    @Test
//    void printSubstringsLeftAlignedLeftTruncatedB() {
//        String stringToSubstring = "cagtc";
//        String expectedPrint =
//                "cagtc" + System.lineSeparator() +
//                        "cagt" + System.lineSeparator() +
//                        "cag" + System.lineSeparator() +
//                        "ca" + System.lineSeparator() +
//                        "c" + System.lineSeparator();
//        asp.printSubstringsLeftAlignedLeftTruncated(stringToSubstring);
//        assertEquals(expectedPrint, outContent.toString());
//    }

    @Test
    @DisplayName("Test substring printing left aligned left truncated")
    public void printAllSubstrings_A() {
        String stringToSubstring = "GATCG";
        boolean leftTruncated = true;
        boolean leftAligned = true;
        String expectedPrint =
                "GATCG" + System.lineSeparator() +
                "ATCG" + System.lineSeparator() +
                "TCG" + System.lineSeparator() +
                "CG" + System.lineSeparator() +
                "G" + System.lineSeparator();
        asp.printAllSubstrings(stringToSubstring, leftTruncated, leftAligned);
        assertEquals(expectedPrint, outContent.toString());
    }

    @Test
    @DisplayName("Test substring printing left aligned right truncated")
    public void printAllSubstrings_B() {
        String stringToSubstring = "GATCG";
        boolean leftTruncated = false;
        boolean leftAligned = true;
        String expectedPrint =
                "GATCG" + System.lineSeparator() +
                "GATC" + System.lineSeparator() +
                "GAT" + System.lineSeparator() +
                "GA" + System.lineSeparator() +
                "G" + System.lineSeparator();
        asp.printAllSubstrings(stringToSubstring, leftTruncated, leftAligned);
        assertEquals(expectedPrint, outContent.toString());
    }

    @Test
    @DisplayName("Test substring printing right aligned right truncated")
    public void printAllSubstrings_C() {
        String stringToSubstring = "AGCGCT";
        boolean leftTruncated = false;
        boolean leftAligned = false;
        String expectedPrint =
                "AGCGCT" + System.lineSeparator() +
                " AGCGC" + System.lineSeparator() +
                "  AGCG" + System.lineSeparator() +
                "   AGC" + System.lineSeparator() +
                "    AG" + System.lineSeparator() +
                "     A" + System.lineSeparator();
        asp.printAllSubstrings(stringToSubstring, leftTruncated, leftAligned);
        assertEquals(expectedPrint, outContent.toString());
    }

    @Test
    @DisplayName("Test substring printing right aligned left truncated")
    public void printAllSubstrings_D() {
        String stringToSubstring = "AGCGCT";
        boolean leftTruncated = true;
        boolean leftAligned = false;
        String expectedPrint =
                "AGCGCT" + System.lineSeparator() +
                " GCGCT" + System.lineSeparator() +
                "  CGCT" + System.lineSeparator() +
                "   GCT" + System.lineSeparator() +
                "    CT" + System.lineSeparator() +
                "     T" + System.lineSeparator();
        asp.printAllSubstrings(stringToSubstring, leftTruncated, leftAligned);
        assertEquals(expectedPrint, outContent.toString());
    }

    @BeforeEach
    public void setUpStreams() {
        System.setOut(new PrintStream(outContent));
    }

    @AfterEach
    public void cleanUpStreams() {
        System.setOut(null);
    }
}