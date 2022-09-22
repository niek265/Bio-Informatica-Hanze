package snippets.apis;

import java.util.Comparator;

public class BirdNameComparator implements Comparator<Bird> {
    @Override
    public int compare(Bird first, Bird second) {
        return first.englishName.compareTo(second.englishName);
    }
}
