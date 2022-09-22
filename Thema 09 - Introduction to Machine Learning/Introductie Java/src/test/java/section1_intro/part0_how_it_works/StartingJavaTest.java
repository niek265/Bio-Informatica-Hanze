package section1_intro.part0_how_it_works;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.assertEquals;


/**
 * Creation date: Jun 26, 2017
 *
 * @version 0.01
 * @author Michiel Noback (&copy; 2017)
 */
public class StartingJavaTest {
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private StartingJava startingJava = null;

    @BeforeEach
    public void setUpStreams() {
        startingJava = new StartingJava();
    }

    @Test
    public void testPrintHelloWorld() {
        PrintStream sysOut = System.out;
        System.setOut(new PrintStream(outContent));
        startingJava.printHelloWorld();
        String printedResult = outContent.toString();
        sysOut.print(printedResult);
        assertEquals("Hello, World", printedResult);
        System.setOut(sysOut);
    }

    @Test
    public void testPrintHelloUser() {
        PrintStream sysOut = System.out;
        System.setOut(new PrintStream(outContent));
        startingJava.printHelloUser();
        String printedResult = outContent.toString();
        sysOut.print(printedResult);
        String expectedResult = "Hello, " + System.getProperty("user.name") + "!";
        assertEquals(expectedResult, printedResult);
        System.setOut(sysOut);
    }

    @Test
    public void testAddInts() {
        int x = 2;
        int y = 4;
        int result = x + y;
        assertEquals(result, startingJava.addInts(x, y));

        x = -10;
        y = 6;
        result = x + y;
        assertEquals(result, startingJava.addInts(x, y));
    }

    @Test
    public void testCalculateSpeed() {
        //using AssertJ assertions
        assertThat(startingJava.calculateSpeed(1000, 120))
                .isEqualTo(30.0);
        assertThat(startingJava.calculateSpeed(100000, 3600))
                .isEqualTo(100.0);
    }

    @Test
    public void testDivideAndRound() {
        double x = 4.999;
        double y = 1.999;
        long result = 3;
        assertEquals(result, startingJava.divideAndRound(x, y));

        y = 2.001;
        result = 2;
        assertEquals(result, startingJava.divideAndRound(x, y));
    }

    @Test
    public void testGetGreeting() {
        assertEquals("Wazzup", startingJava.getGreeting(2));
        assertEquals("Yo!", startingJava.getGreeting(3));
    }

    @Test
    public void testCreateDuck() {
        int speed = 7;
        String name = "Shelduck";
        Duck duck = startingJava.createDuck(speed, name);

        assertEquals(7, duck.swimSpeed);
        assertEquals(name, duck.name);

        speed = 2;
        name = "Common Mallard";
        duck = startingJava.createDuck(speed, name);

        assertEquals(2, duck.swimSpeed);
        assertEquals(name, duck.name);
    }
}