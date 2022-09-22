package section1_intro.part1_language_basics;

import java.text.NumberFormat;

public class GeometryAnalyser {
    public static void main(String[] args) {
        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        int c = Integer.parseInt(args[2]);
        int d = Integer.parseInt(args[3]);
        String method = args[4];

        if (method == "surf") {
            Rectangle rectangle = new Rectangle();
            rectangle.upperLeft = new Point();
            rectangle.lowerRight = new Point();
            rectangle.upperLeft.x = a;
            rectangle.upperLeft.y = b;
            rectangle.lowerRight.x = c;
            rectangle.lowerRight.y = d;

            int answer = rectangle.getSurface();
            System.out.println(answer);
        } else if (method == "dist") {
            Point point = new Point();
            Point otherPoint = new Point();
            point.x = a;
            point.y = b;
            otherPoint.x = c;
            otherPoint.y = d;

            double answer = point.euclideanDistanceTo(otherPoint);
            NumberFormat numberFormat = NumberFormat.getNumberInstance();
            numberFormat.setMaximumFractionDigits(1);
            System.out.println(numberFormat.format(answer));

        } else {
            System.out.println("error");
        }
    }
}
