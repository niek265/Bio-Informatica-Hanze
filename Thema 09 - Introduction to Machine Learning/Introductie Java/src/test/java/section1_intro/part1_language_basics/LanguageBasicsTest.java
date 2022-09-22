package section1_intro.part1_language_basics;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.offset;
import static org.junit.jupiter.api.Assertions.*;

class LanguageBasicsTest {
    private LanguageBasics languageBasics;

    @BeforeEach
    void setUp(){
        this.languageBasics = new LanguageBasics();
    }

    @Test
    void isMultiple() {
        assertTrue(languageBasics.isMultiple(9, 3));
        assertTrue(languageBasics.isMultiple(15, 5));
        assertFalse(languageBasics.isMultiple(9, 2));
        assertFalse(languageBasics.isMultiple(10, 3));
    }

    @Test
    void getDistanceInMeters() {
        assertThat(languageBasics.
                getDistanceInMeters(100, 30)).
                isEqualTo(50000, offset(1e-6));
        assertThat(languageBasics.
                getDistanceInMeters(50, 12)).
                isEqualTo(10000, offset(1e-6));
    }

    @Test
    void getCumulativeSum() {
        assertThat(languageBasics.getCumulativeSum(5)).isEqualTo(15);
        assertThat(languageBasics.getCumulativeSum(10)).isEqualTo(55);
    }

    @Test
    void getTheAbsolutePower() {
        assertThat(languageBasics.getTheAbsolutePower(5, 3)).isEqualTo(125);
        assertThat(languageBasics.getTheAbsolutePower(5, -3)).isEqualTo(125);
        assertThat(languageBasics.getTheAbsolutePower(2, 2)).isEqualTo(4);
        assertThat(languageBasics.getTheAbsolutePower(-2, 2)).isEqualTo(4);
        assertThat(languageBasics.getTheAbsolutePower(-2, -3)).isEqualTo(-8);
    }

    @Test
    void returnCorrectlyNamedVariable_1() {
        String value = this.languageBasics.returnCorrectlyNamedVariable_1();
        assertEquals("Louis XIV, le Roi Soleil", value);
    }

    @Test
    void returnCorrectlyNamedVariable_2() {
        String value = this.languageBasics.returnCorrectlyNamedVariable_2();
        assertThat(value).isEqualTo("D");
    }

    @Test
    void returnCorrectlyNamedVariable_3() {
        String value = this.languageBasics.returnCorrectlyNamedVariable_3();
        assertThat(value).isEqualTo("B");
    }

}