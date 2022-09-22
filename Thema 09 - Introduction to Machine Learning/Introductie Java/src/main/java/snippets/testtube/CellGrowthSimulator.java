package snippets.testtube;

/**
 * "Controller" class
 */
public class CellGrowthSimulator {
    /**
     *
     * @param args cl-args should be length one, containing initial cell number.
     */
    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("You must provide an initial cell count. Aborting.");
        }


        int initialCellNumber = Integer.parseInt(args[0]);
        startSimulation(initialCellNumber);
    }

    private static void startSimulation(int initialCellNumber) {
        TestTube testTube = new TestTube(initialCellNumber);
        //do one iteration of growing
        testTube.growCells();
    }
}
