package snippets.testtube2;

import java.util.ArrayList;
import java.util.List;

public class TestTube {
    private final int numberOfLifeCyclesToRun;
    private final int initialCellCount;
    private List<Cell> cells = new ArrayList<>();
    private int defaultCellDiameter = 20;
    private int defaultSizeIncrement = 2;

    /**
     * Constructs with the two essential parameters
     * @param numberOfLifeCyclesToRun a number between 1 and 100
     * @param initialCellCount a number between 1 and 1000
     */
    public TestTube (int numberOfLifeCyclesToRun, int initialCellCount) {
        if (numberOfLifeCyclesToRun < 1
                || numberOfLifeCyclesToRun > 100
                || initialCellCount < 1
                || initialCellCount > 1000) {
            throw new IllegalArgumentException("Number of life cycles should be between 1 and 100 and initial cell " +
                    "count between 1 and 1000");
        }
        this.numberOfLifeCyclesToRun = numberOfLifeCyclesToRun;
        this.initialCellCount = initialCellCount;
    }

    /**
     * sets the initial diameter of instantiated cells.
     * @param defaultCellDiameter the cell default diameter in micrometers
     */
    public void setDefaultCellDiameter(int defaultCellDiameter) {
        this.defaultCellDiameter = defaultCellDiameter;
    }

    /**
     * Sets the size increment for cell growth
     * @param defaultSizeIncrement the cell size increment in micrometers
     */
    public void setDefaultSizeIncrement(int defaultSizeIncrement) {
        this.defaultSizeIncrement = defaultSizeIncrement;
    }

    /**
     * starts the growth process
     */
    public void start() {
        initializeCells();
        runLifeCycles();
    }

    private void runLifeCycles() {
        for (int i = 0; i < this.numberOfLifeCyclesToRun; i++) {
            growCells();
        }
    }

    private void initializeCells() {
        for (int i = 0; i < this.initialCellCount; i++) {
            cells.add(new Cell(this.defaultCellDiameter, this.defaultSizeIncrement));
        }
    }

    private void growCells() {
        for (Cell cell : this.cells) {
            cell.grow();
        }
        //since Java 8, this is also possible:
        //this.cells.forEach(c -> c.grow());
        //or
        //this.cells.forEach(Bacterium::grow);
    }
}
