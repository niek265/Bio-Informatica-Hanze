package section3_apis.part2_collections;

import org.junit.jupiter.api.Test;

import java.util.*;

import static org.junit.jupiter.api.Assertions.assertEquals;

class FindTheRightCollectionTest {
    final FindTheRightCollection findTheRightCollection = new FindTheRightCollection();

    @Test
    void findTheRightCollection1() {
        assertEquals(ArrayList.class, findTheRightCollection.rightCollection1());
    }

    @Test
    void findTheRightCollection2() {
        assertEquals(HashMap.class, findTheRightCollection.rightCollection2());
    }

    @Test
    void findTheRightCollection3() {
        assertEquals(LinkedList.class, findTheRightCollection.rightCollection3());
    }

    @Test
    void findTheRightCollection4() {
        assertEquals(HashSet.class, findTheRightCollection.rightCollection4());
    }

    @Test
    void findTheRightCollection5() {
        assertEquals(List.class, findTheRightCollection.rightCollection5());
    }

    @Test
    void findTheRightCollection6() {
        assertEquals(Set.class, findTheRightCollection.rightCollection6());
    }

    @Test
    void findTheRightCollection7() {
        assertEquals(Map.class, findTheRightCollection.rightCollection7());
    }

    @Test
    void findTheRightCollection8() {
        assertEquals(TreeSet.class, findTheRightCollection.rightCollection8());
    }

}