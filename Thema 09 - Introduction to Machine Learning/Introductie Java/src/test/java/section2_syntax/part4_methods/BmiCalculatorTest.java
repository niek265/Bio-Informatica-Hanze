package section2_syntax.part4_methods;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class BmiCalculatorTest {
    private final static double DELTA = 0.001;
    @Test
    public void testCalculateBMI_A() {
        BmiCalculator instance = new BmiCalculator();
        double weight = 80.0;
        double lenght = 1.80;
        double expResult = (weight / (lenght * lenght));
        double result = instance.calculateBMI(weight, lenght);
        assertEquals(expResult, result, DELTA);
    }

    @Test
    public void testCalculateBMI_B() {
        BmiCalculator instance = new BmiCalculator();
        double weight = 49.0;
        double lenght = 1.56;
        double expResult = (weight / (lenght * lenght));
        double result = instance.calculateBMI(weight, lenght);
        assertEquals(expResult, result, DELTA);
    }

    @Test
    public void testCalculateBMI_C() {
        BmiCalculator instance = new BmiCalculator();
        double weight = 80.0;
        double lenght = 0.0;
        try {
            instance.calculateBMI(weight, lenght);
            fail("expected " + IllegalArgumentException.class.getName());
        } catch (IllegalArgumentException ex) {
            return;
        }
    }

    @Test
    public void testCalculateBMI_D() {
        BmiCalculator instance = new BmiCalculator();
        double weight = -10.0;
        double lenght = 1.75;
        try {
            instance.calculateBMI(weight, lenght);
            fail("expected " + IllegalArgumentException.class.getName());
        } catch (IllegalArgumentException ex) {
            return;
        }
    }

    @Test
    public void testGetMessage_A() {
        double bmi = 17.0;
        BmiCalculator instance = new BmiCalculator();
        String expResult = "Ondergewicht";
        String result = instance.getMessage(bmi);
        assertEquals(expResult, result);
    }

    @Test
    public void testGetMessage_B() {
        double bmi = 42.50;
        BmiCalculator instance = new BmiCalculator();
        String expResult = "Morbide Obesitas";
        String result = instance.getMessage(bmi);
        assertEquals(expResult, result);
    }

    @Test
    public void testGetMessage_C() {
        double bmi = 20.50;
        BmiCalculator instance = new BmiCalculator();
        String expResult = "Gezond gewicht";
        String result = instance.getMessage(bmi);
        assertEquals(expResult, result);
    }

    @Test
    public void testGetMessage_D() {
        double bmi = 28.10;
        BmiCalculator instance = new BmiCalculator();
        String expResult = "Overgewicht";
        String result = instance.getMessage(bmi);
        assertEquals(expResult, result);
    }

    @Test
    public void testGetMessage_E() {
        double bmi = 39.99;
        BmiCalculator instance = new BmiCalculator();
        String expResult = "Obesitas";
        String result = instance.getMessage(bmi);
        assertEquals(expResult, result);
    }

    @Test
    public void testGetMessage_F() {
        double bmi = -1.0;
        BmiCalculator instance = new BmiCalculator();
        try {
            instance.getMessage(bmi);
            fail("expected " + IllegalArgumentException.class.getName());
        } catch (IllegalArgumentException ex) {
            assertTrue(true);
        }
    }
}