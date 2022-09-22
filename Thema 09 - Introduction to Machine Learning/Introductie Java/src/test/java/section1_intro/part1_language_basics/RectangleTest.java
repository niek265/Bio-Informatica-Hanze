package section1_intro.part1_language_basics;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class RectangleTest {

    @Test
    void surface() {
        Point p1 = new Point();
        p1.x = 2;
        p1.y = 8;

        Point p2 = new Point();
        p2.x = 10;
        p2.y = 3;

        Rectangle rectangle = new Rectangle();
        rectangle.upperLeft = p1;
        rectangle.lowerRight = p2;

        assertEquals((5*8), rectangle.getSurface());

        p1.x = 5;
        p1.y = 12;
        p2.x = 8;
        p2.y = 1;

        assertEquals((11*3), rectangle.getSurface());
    }
}
