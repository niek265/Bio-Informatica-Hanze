package snippets.testtube2;

public class CellGrowthSimulator {
    private static TestTube testTube;

    public static void main(String[] args) {
        startSimulation();
    }

    private static void startSimulation() {
        testTube = new TestTube(10,5);
        testTube.setDefaultCellDiameter(10);
        testTube.start();
    }
}
