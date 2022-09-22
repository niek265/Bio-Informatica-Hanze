package section2_syntax.part2_operators;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;

class WeightUnitsSolverTest {

    @DisplayName("Conversion test with multiple inputs")
    @ParameterizedTest(name = "{0} should give {1} pounds, {2} ounces, {3} grams")
    @CsvSource({"1,0,0,1", "1000,2,3,8", "25369,55,14,7"})
    void convertFromGrams(int inputGrams, int pounds, int ounces, int grams) {
        WeightUnitsSolver instance = new WeightUnitsSolver();
        BritishWeightUnits observed = instance.convertFromGrams(inputGrams);
        assertThat(observed.getPounds()).isEqualTo(pounds);
        assertThat(observed.getOunces()).isEqualTo(ounces);
        assertThat(observed.getGrams()).isEqualTo(grams);
    }

    @Test
    @DisplayName("Test conversion with illegal argument")
    public void testConvertFromGrams_D() {
        int grams = -1;
        WeightUnitsSolver instance = new WeightUnitsSolver();
        try {
            instance.convertFromGrams(grams);
            fail(String.format("Testing unit conversion with %d; grams ... expected %s", grams, IllegalArgumentException.class.getName()));
        } catch (IllegalArgumentException ex) {
            return;
        }
    }
}