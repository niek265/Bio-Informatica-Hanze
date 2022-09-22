package snippets.apis;

public class Bird implements Comparable<Bird>{
    String englishName;
    double wingSpan;
    int maximumAge;

    public Bird(String englishName, double wingSpan, int maximumAge) {
        this.englishName = englishName;
        this.wingSpan = wingSpan;
        this.maximumAge = maximumAge;
    }

    @Override
    public String toString() {
        return englishName + '\'' +
                ", ws=" + wingSpan +
                ", max.age=" + maximumAge;
    }


    @Override
    public int compareTo(Bird other) {
        final int compareWingSpan = Double.compare(this.wingSpan, other.wingSpan);
        if (compareWingSpan == 0) {
            return this.englishName.compareTo(other.englishName);
        }
        return compareWingSpan;

        //return Double.compare(this.wingSpan, other.wingSpan);


//        final int BEFORE = -1;
//        final int EQUAL = 0;
//        final int AFTER = 1;
//        if(this.wingSpan <= other.wingSpan) return AFTER;
//        else if (this.wingSpan >= other.wingSpan) return BEFORE;
//        else return EQUAL;
    }
}
