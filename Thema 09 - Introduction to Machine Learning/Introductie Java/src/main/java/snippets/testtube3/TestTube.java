package snippets.testtube3;

import java.util.ArrayList;
import java.util.List;

public class TestTube {
    private final int numberOfLifeCyclesToRun;
    private final int initialCellCount;
    private final String cellType;
    private List<Cell> cells = new ArrayList<>();

    /**
     * Constructs with the two essential parameters
     * @param numberOfLifeCyclesToRun a number between 1 and 100
     * @param initialCellCount a number between 1 and 1000
     * @param cellType the cell type ["
     */
    public TestTube (int numberOfLifeCyclesToRun, int initialCellCount, String cellType) {
        //check code omitted
        this.numberOfLifeCyclesToRun = numberOfLifeCyclesToRun;
        this.initialCellCount = initialCellCount;
        this.cellType = cellType;
    }

    /**
     * starts the growth process
     */
    public void start() {
        initializeCells();
        runLifeCycles();
    }

    private void runLifeCycles() {
        for (int i = 1; i <= this.numberOfLifeCyclesToRun; i++) {
            growCells();
            if (i % 10 == 0) System.out.println("Grow cycle " + i + " finished; " + cells.size() + " cells present");
        }
    }

    private void initializeCells() {
        for (int i = 0; i < this.initialCellCount; i++) {
            cells.add(Cell.of(cellType));
        }
    }

    private void growCells() {
        //I have no clue what is growing here and don't care
        //enhanced for loop will cause a ConcurrentModificationException
        for (int i = 0; i < cells.size(); i++) {
            Cell cell = cells.get(i);
            Cell child = cell.grow();
            if (child != null) cells.add(child);
            if (cell instanceof WhiteBloodCell) {
                WhiteBloodCell wbc = (WhiteBloodCell)cell;
                wbc.eatOtherCell(child);
            }
        }
    }
}
