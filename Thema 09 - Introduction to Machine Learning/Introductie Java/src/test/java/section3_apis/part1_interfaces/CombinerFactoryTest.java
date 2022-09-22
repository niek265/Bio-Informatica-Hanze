package section3_apis.part1_interfaces;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class CombinerFactoryTest {

    @Test
    void getQuotedCombiner1() {
        final StringCombiner quotedCombiner = CombinerFactory.getQuotedCombiner();
        final String actual = quotedCombiner.combine("foo", "bar");
        final String expected = "'\"foo\" \"bar\"'";
        assertEquals(expected, actual);
    }

    @Test
    void getQuotedCombiner2() {
        final StringCombiner quotedCombiner = CombinerFactory.getQuotedCombiner();
        final String actual = quotedCombiner.combine("how", "dy");
        final String expected = "'\"how\" \"dy\"'";
        assertEquals(expected, actual);
    }

    @Test
    void getReversedCombiner1() {
        final StringCombiner reversedCombiner = CombinerFactory.getReversedCombiner();
        final String actual = reversedCombiner.combine("foo", "bar");
        final String expected = "foooof barrab";
        assertEquals(expected, actual);
    }

    @Test
    void getReversedCombiner2() {
        final StringCombiner reversedCombiner = CombinerFactory.getReversedCombiner();
        final String actual = reversedCombiner.combine("how", "zow");
        final String expected = "howwoh zowwoz";
        assertEquals(expected, actual);
    }

    @Test
    void getAsciiSumCombiner1() {
        //combiner.combine("one", "two") will return "322 346" (111 + 110 + 101 and 116 + 119 + 111).
        final StringCombiner combiner = CombinerFactory.getAsciiSumCombiner();
        final String actual = combiner.combine("one", "two");
        final String expected = "322 346";
        assertEquals(expected, actual);
    }

    @Test
    void getAsciiSumCombiner2() {
        //combiner.combine("one", "two") will return "322 346" (111 + 110 + 101 and 116 + 119 + 111).
        final StringCombiner combiner = CombinerFactory.getAsciiSumCombiner();
        final String actual = combiner.combine("three", "four");
        final String expected = "536 444"; //116 + 104 + 114 + 101 + 101 = 536 and 102 + 111 + 117 + 114 = 444
        assertEquals(expected, actual);
    }
}