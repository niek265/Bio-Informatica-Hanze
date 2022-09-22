package section1_intro.part1_language_basics;


public class Point {
    int x;
    int y;

    /**
     * Create an instance of class point that is located at the same coordinates as the current object, but in the
     * diagonally opposing quadrant of coordinate space.
     * So, when the current point is at (4, 4), this method will return Point(-4, -4)
     * and when the current point is at (2, -5) it will return Point(-2, 5).
     * @return inverse Point
     */
    Point createInversePoint() {
        Point reverse = new Point();
        reverse.x = x * -1;
        reverse.y = y * -1;
        return reverse;
    }

    /**
     * This method returns the Euclidean distance of the current point (this) to the given point (otherPoint).
     * GIYF if you forgot what Euclidean distance is and how it is calculated.
     * @param otherPoint
     * @return euclidean distance
     */
    double euclideanDistanceTo(Point otherPoint) {
        double one = Math.abs(otherPoint.y - y);
        double two = Math.abs(otherPoint.x - x);
        return Math.hypot(one, two);
    }

    public static void main(String[] args) {
        Point point = new Point();
        point.x = 1;
        point.y = 0;
        System.out.println(point.createInversePoint().x);
        System.out.println(point.createInversePoint().y);

        Point otherPoint = new Point();
        otherPoint.x = 4;
        otherPoint.y = 8;

        System.out.println(point.euclideanDistanceTo(otherPoint));
    };
};
