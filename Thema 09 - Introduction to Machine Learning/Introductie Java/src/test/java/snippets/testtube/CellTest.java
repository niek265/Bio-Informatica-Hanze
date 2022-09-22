package snippets.testtube;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class CellTest {

    @Test
    void grow() {
        Cell cell = new Cell();
        assertTrue(cell.diameter == 5);
        cell.grow();
        assertTrue(cell.diameter == 6);
    }
}
