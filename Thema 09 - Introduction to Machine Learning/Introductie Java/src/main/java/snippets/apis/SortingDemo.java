package snippets.apis;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class SortingDemo {
    public static void main(String[] args) {










        List<String> names = new ArrayList<>();
        names.addAll(List.of("Jordan", "Wanda", "James", "rose", "Aaron"));

        System.out.println("names before sort: " + names);

        Collections.sort(names);

        System.out.println("names after natural sort: " + names);

        names.sort(Comparator.naturalOrder());

        System.out.println("names after sort on List " + names);

        names.sort(String.CASE_INSENSITIVE_ORDER);
        System.out.println("names case insensitive sort " + names);



        names.sort(Comparator.reverseOrder());

        System.out.println("names after reverse sort " + names);



        names.sort(null);
        System.out.println("names after null sort " + names);


        System.exit(0);

        List<Bird> birds = new ArrayList<>();

        birds.add(new Bird("Buzzard", 1.3, 29));
        birds.add(new Bird("Kestrel", 0.35, 15));
        birds.add(new Bird("White-tailed eagle", 2.5, 25));
        birds.add(new Bird("Red kite", 1.8, 23));
        birds.add(new Bird("Steppe eagle", 2.1, 41));
        birds.add(new Bird("Griffon vulture", 2.5, 25));
        birds.add(new Bird("Albatross", 2.5, 25));

        System.out.println("Before:");
        //prints addition order using Java8 streams
        birds.stream().forEach(bird -> System.out.println("\t" + bird));
        Collections.sort(birds);
        System.out.println("After sort on wingspan:");
        //prints sort order on wingspan, ascending
        birds.stream().forEach(bird -> System.out.println("\t" + bird));

        Collections.sort(birds, new BirdNameComparator());
        //print birds sorted on name, alphabetically
        System.out.println("After sort on name:");
        birds.stream().forEach(bird -> System.out.println("\t" + bird));

        Collections.sort(birds, new Comparator<Bird>(){
            @Override
            public int compare(Bird first, Bird second) {
                return Integer.compare(first.maximumAge, second.maximumAge);
            }
        });
        System.out.println("After sort on maximum age:");
        birds.stream().forEach(bird -> System.out.println("\t" + bird));

        //Java8+ alternative: OK
        Collections.sort(birds, (birdOne, birdTwo) -> Integer.compare(birdOne.maximumAge, birdTwo.maximumAge));
        //Java8+ alternative: best
        Collections.sort(birds, Comparator.comparingInt(bird -> bird.maximumAge));


        //using Java8+ feature
        //birds.sort(Comparator.comparingDouble(bird -> bird.wingSpan));
        birds.sort(new BirdNameComparator());

    }

}
