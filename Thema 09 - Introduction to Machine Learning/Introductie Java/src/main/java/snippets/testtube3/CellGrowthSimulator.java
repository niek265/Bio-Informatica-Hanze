package snippets.testtube3;

public class CellGrowthSimulator {
    private static TestTube testTube;

    public static void main(String[] args) {
        startSimulation();
    }

    private static void startSimulation() {
        testTube = new TestTube(100,5, "Bacteria");
        testTube.start();
    }
}
