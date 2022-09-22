/*
 * Copyright (c) 2015 Michiel Noback [michiel.noback@gmail.com].
 * All rights reserved.
 */
package section4_oop.part1_inheritance;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 *
 * @author Michiel Noback [michiel.noback@gmail.com]
 */
public class AnimalSimulatorTest {

    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();

    @BeforeEach
    public void setUpStreams() {
        System.setOut(new PrintStream(outContent));
    }

    @AfterEach
    public void cleanUpStreams() {
        System.setOut(null);
    }

    /**
     * tests empty argument array
     */
    @Test
    public void testMain_A() {
        String[] args = new String[]{};
        String expectedPrint
                = "Usage: java AnimalSimulator <Species age Species age ...>" + System.lineSeparator()
                + "Supported species (in alphabetical order):" + System.lineSeparator()
                + "1: Elephant" + System.lineSeparator()
                + "2: Horse" + System.lineSeparator()
                + "3: Mouse" + System.lineSeparator()
                + "4: Tortoise" + System.lineSeparator();
        AnimalSimulator.main(args);
        assertEquals(expectedPrint, outContent.toString());
    }

    /**
     * tests argument array with only element "help"
     */
    @Test
    public void testMain_B() {
        String[] args = new String[]{"help"};
        String expectedPrint
                = "Usage: java AnimalSimulator <Species age Species age ...>" + System.lineSeparator()
                + "Supported species (in alphabetical order):" + System.lineSeparator()
                + "1: Elephant" + System.lineSeparator()
                + "2: Horse" + System.lineSeparator()
                + "3: Mouse" + System.lineSeparator()
                + "4: Tortoise" + System.lineSeparator();
        AnimalSimulator.main(args);
        assertEquals(expectedPrint, outContent.toString());
    }

    /**
     * tests argument array with "Horse 21"
     * A Horse of age 21 moving in gallop at 73.1 km/h
     */
    @Test
    public void testMain_C() {
        String[] args = new String[]{"Horse", "21"};
        String expectedPrint
                = "A Horse of age 21 moving in gallop at 73.1 km/h" + System.lineSeparator();
        AnimalSimulator.main(args);
        assertEquals(expectedPrint, outContent.toString());
    }

    /**
     * tests argument array with "Horse 21 Elephant 2"
     */
    @Test
    public void testMain_D() {
        String[] args = new String[]{"Horse", "21", "Elephant", "2"};
        String expectedPrint
                = "A Horse of age 21 moving in gallop at 73.1 km/h" + System.lineSeparator()
                + "An Elephant of age 2 moving in thunder at 39.5 km/h" + System.lineSeparator();
        AnimalSimulator.main(args);
        assertEquals(expectedPrint, outContent.toString());
    }

    /**
     * tests argument array with "Mouse 12"
     */
    @Test
    public void testMain_E() {
        String[] args = new String[]{"Mouse", "12"};
        String expectedPrint
                = "A Mouse of age 12 moving in scurry at 11.3 km/h" + System.lineSeparator();
        AnimalSimulator.main(args);
        assertEquals(expectedPrint, outContent.toString());
    }

    /**
     * tests argument array with "Pouse 11"
     */
    @Test
    public void testMain_F() {
        String[] args = new String[]{"Pouse", "11"};
        String expectedPrint
                = "Error: animal species Pouse is not known. run with single parameter \"help\" to get a listing of available species. Please give new values" + System.lineSeparator();
        AnimalSimulator.main(args);
        assertEquals(expectedPrint, outContent.toString());
    }

    /**
     * tests argument array with "Mouse 18"
     */
    @Test
    public void testMain_G() {
        String[] args = new String[]{"Mouse", "18"};
        String expectedPrint
                = "Error: maximum age of Mouse is 13 years. Please give new values" + System.lineSeparator();
        AnimalSimulator.main(args);
        assertEquals(expectedPrint, outContent.toString());
    }

    /**
     * tests the supported animals
     */
    @Test
    public void testGetSupportedAnimals() {
        AnimalSimulator instance = new AnimalSimulator();
        List<String> expResult = Arrays.asList(new String[]{"Elephant", "Horse", "Mouse", "Tortoise"});
        List<String> result = instance.getSupportedAnimals();
        assertEquals(expResult, result);
    }

}
