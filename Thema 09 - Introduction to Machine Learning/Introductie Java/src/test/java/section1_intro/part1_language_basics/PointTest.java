package section1_intro.part1_language_basics;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class PointTest {

    @Test
    @DisplayName("Test whether the inverse point has been created correctly")
    void testCreateInversePoint() {
        Point point = new Point();
        point.x = 1;
        point.y = 0;
        assertThat(point.createInversePoint().x).isEqualTo(-1);
        assertThat(point.createInversePoint().y).isEqualTo(0);
        point.x = 2;
        point.y = -3;
        assertThat(point.createInversePoint().x).isEqualTo(-2);
        assertThat(point.createInversePoint().y).isEqualTo(3);
        point.x = -1;
        point.y = -3;
        assertThat(point.createInversePoint().x).isEqualTo(1);
        assertThat(point.createInversePoint().y).isEqualTo(3);
    }

    @Test
    @DisplayName("Tests to verify the Euclidean distance calculation (1)")
    void distanceToIsZero() {
        Point p1 = new Point();
        p1.x = 0;
        p1.y = 0;

        Point p2 = new Point();
        p2.x = 0;
        p2.y = 0;

        assertEquals(0, p2.euclideanDistanceTo(p1));
    }

    @Test
    @DisplayName("Tests to verify the Euclidean distance calculation (2)")
    void distanceToIsNonZero() {
        Point p1 = new Point();
        p1.x = 2;
        p1.y = 2;

        Point p2 = new Point();
        p2.x = 4;
        p2.y = 4;

        assertEquals(Math.sqrt(8), p2.euclideanDistanceTo(p1));
    }

}
