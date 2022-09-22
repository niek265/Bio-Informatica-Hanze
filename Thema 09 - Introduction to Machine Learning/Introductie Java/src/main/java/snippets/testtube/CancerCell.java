package snippets.testtube;

public class CancerCell extends Cell {
    CancerCell() {
        growthIncrement = 3;
    }

    void move() {
        System.out.println("Moving through the body");
    }
}
