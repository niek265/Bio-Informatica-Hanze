package section1_intro.part1_language_basics;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import section2_syntax.part3_flow_control.AllSubstringsPrinter;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.is;
import static org.hamcrest.Matchers.anyOf;
import static org.junit.jupiter.api.Assertions.assertEquals;

class GeometryAnalyserTest {


    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private final AllSubstringsPrinter asp = new AllSubstringsPrinter();

    @BeforeEach
    public void setUpStreams() {
        System.setOut(new PrintStream(outContent));
    }

    @AfterEach
    public void cleanUpStreams() {
        System.setOut(null);
    }


    @Test
    void mainSurfaceTest1() {
        String[] commandLineArgs = {"2", "5", "6", "2", "surf"};
        GeometryAnalyser.main(commandLineArgs);
        String expectedOutput = "12" + System.lineSeparator();
        String observedOutput = outContent.toString();
        assertEquals(expectedOutput, observedOutput);
    }

    @Test
    void mainSurfaceTest2() {
        String[] commandLineArgs = {"7", "10", "17", "0", "surf"};
        GeometryAnalyser.main(commandLineArgs);
        String expectedOutput = "100" + System.lineSeparator();
        String observedOutput = outContent.toString();
        assertEquals(expectedOutput, observedOutput);
    }

    @Test
    void mainDistanceTest2() {
        String[] commandLineArgs = {"2", "5", "6", "2", "dist"};
        GeometryAnalyser.main(commandLineArgs);
        String expectedOutput1 = "5" + System.lineSeparator();
        String expectedOutput2 = "5.0" + System.lineSeparator();
        String expectedOutput3 = "5,0" + System.lineSeparator();
        String observedOutput = outContent.toString();
        assertThat(observedOutput, anyOf(org.hamcrest.Matchers.is(expectedOutput1), is(expectedOutput2), is(expectedOutput3)));
    }

    @Test
    void mainDistanceTest3() {
        String[] commandLineArgs = {"1", "8", "5", "12", "dist"};
        GeometryAnalyser.main(commandLineArgs);
        String expectedOutput1 = "5,7" + System.lineSeparator();
        String expectedOutput2 = "5.7" + System.lineSeparator();
        String observedOutput = outContent.toString();
        assertThat(observedOutput, anyOf(org.hamcrest.Matchers.is(expectedOutput1), is(expectedOutput2)));//Equals(expectedOutput, observedOutput);
    }

}