package snippets.apis;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class CollectionsDemoTest {

    @Test
    void mapOperations() {
        CollectionsDemo cd = new CollectionsDemo();
        cd.mapOperations();
    }

    @Test
    void toStringTest() {
        CollectionsDemo cd = new CollectionsDemo();
        cd.equalsAndHashCode();
    }
}