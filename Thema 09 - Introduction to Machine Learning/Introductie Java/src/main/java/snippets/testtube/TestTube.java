package snippets.testtube;

public class TestTube {
    Cell[] cells;

    /**
     * Constructs with an initial cell count.
     * An exception is thrown when the initial cell count is below 1 or above 10e4.
     *
     * @param initialCellCount the initial cell count
     * @throws IllegalArgumentException ex
     */
    public TestTube(int initialCellCount) {
        if (initialCellCount == 0 || initialCellCount > 10e4) {
            throw new IllegalArgumentException("initial cell count should be above 1 and below 10e4: " + initialCellCount);
        }
        //initialize the array with new Cells
        cells = new Cell[initialCellCount];
        for (int i = 0; i < initialCellCount; i++) {
            cells[i] = new Cell();
        }
    }

    /**
     * Grows the cells, in one single iteration.
     */
    public void growCells() {
        for (Cell cell : cells) {
            cell.grow();
        }
    }
}
