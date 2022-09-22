package snippets.apis;

import snippets.syntax.Duck;

import java.util.*;

public class CollectionsDemo {
    public static void main(String[] args) {
        setOperations();
    }

    private static void setOperations() {
        Set<Integer> setA = setOf(1,2,3,4);
        Set<Integer> setB = setOf(2,4,6,8,9);

        //Intersection
        Set<Integer> intersectSet = new HashSet<>(setA);
        intersectSet.retainAll(setB);
        System.out.println("intersectSet = " + intersectSet);

        //Union
        Set<Integer> unionSet = new HashSet<>(setA);
        unionSet.addAll(setB);
        System.out.println("unionSet = " + unionSet);

        //Relative complement
        Set<Integer> differenceSet = new HashSet<>(setA);
        differenceSet.removeAll(setB);
        System.out.println("differenceSet = " + differenceSet);
    }

    private static <T> Set<T> setOf(T... values) {
        return new HashSet<T>(Arrays.asList(values));
    }

    void listOperations() {
        //typed collection
//        ArrayList<String> words = new ArrayList<>();

        //better
//        List<String> words = new ArrayList<>();
        List<String> words = new LinkedList<>();


        words.add("Game");
        words.add("of");
        words.add("Thrones");
//        words.add(new Duck());

        for (String word : words) {
            System.out.println("word = " + word);
        }
        //type is inferred from collection
        for (int i = 0; i < words.size(); i++) {
            String word = words.get(i);
            System.out.println("word = " + i + ": " + word);
        }

        words.contains("Thrones"); //true
        words.size(); //3
        words.isEmpty(); //false
        //same as
        boolean empty = words.size() == 0;

        words.remove("of"); //deletes word
        words.remove(1); //second element
        words.clear(); //empty list


        //"raw" type collection: everything is Object
        ArrayList wordsNonGeneric = new ArrayList();
        wordsNonGeneric.add("House");
        wordsNonGeneric.add("of");
        wordsNonGeneric.add("Cards");
        //danger!
        wordsNonGeneric.add(new Duck());

        //iterate over Object type
        for (int i = 0; i < wordsNonGeneric.size(); i++) {
            //need to cast to actual type
            //this will give a ClassCastException exception on the Duck, which is of course not a String!
            Object element = wordsNonGeneric.get(i);
            if (element instanceof String) {
                String word = (String) element;
                System.out.println("word = " + i + ": " + word);
            } else {
                System.out.println("skipped non-String element of type " + element.getClass().getSimpleName());
            }
        }

        String[] wordsArr = {"Lord", "of", "the", "Rings"};
        //create immutable List from Array
        List<String> immutableStrings = Arrays.asList(wordsArr);
        //immutable: UnsupportedOperationException!
        //immutableStrings.add("!");
        //make mutable copy
        List<String> mutableString = new ArrayList<>();
        //no problem
        mutableString.add("!");
    }

    void autoboxingWrappers() {
        int count = 33;

        //deprecated though legal
        //Integer counter1 = new Integer(count);
        //OK, be explicit; uses caching
        Integer counter2 = Integer.valueOf(count);
        //explicit unwrapping
        counter2.intValue();

        //autoboxing!
        Integer counter3 = count;
        //auto-unboxing
        int counter4 = counter3;
    }

    void mapOperations() {
        Map<Integer, User> users = new HashMap<>();
        User u1 = new User(15, "Henk");
        //add to Map
        users.put(u1.id, u1);
        User u2 = new User(21, "Dirk");
        users.put(u2.id, u2);
        User u3 = new User(9, "Mike");
        users.put(u3.id, u3);

        //read size
        System.out.println(users.size());
        //check for presence of key
        System.out.println("users.containsKey(15) = " + users.containsKey(15));
        //check for presence of value
        System.out.println("users.containsValue() = " + users.containsValue(u1));
        //is not in map
        System.out.println("users.containsValue() = " + users.containsValue(new User(6, "Nick")));

        for (User user : users.values()) {
            //iterate values
        }

        for (int id : users.keySet()) {
            //iterate keys
        }

        for (Map.Entry<Integer, User> entry : users.entrySet()) {
            //iterate entries
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }

        //empties map
        users.clear();
    }


    void equalsAndHashCode() {

        User user1 = new User(15, "Henk");
        //same, equal?
        User user2 = user1;

        User user3 = new User(21, "Dirk");
        //same, or equal User as user3?
        User user4 = new User(21, "Dirk");

        System.out.println("user1 == user1 -- " + (user1 == user1)); //should be true
        System.out.println("user1.equals(user1) -- " + user1.equals(user1)); //should be true
        System.out.println("user1 == user2 -- " + (user1 == user2)); //should be true
        System.out.println("user1.equals(user2) -- " + user1.equals(user2)); //should be true
        System.out.println("user1.equals(user3) -- " + user1.equals(user3)); //should be false
        System.out.println("user3.equals(user4) -- " + user3.equals(user4)); //should be true!

        System.out.println(user1);

        System.out.println("user1.getClass().getSimpleName() = " + user1.getClass().getSimpleName());
        System.out.println("user1.getClass().getCanonicalName() = " + user1.getClass().getCanonicalName());
        System.out.println("user1.getClass().getName() = " + user1.getClass().getName());
        System.out.println("user1.getClass().getPackageName() = " + user1.getClass().getPackageName());
        System.out.println("user1.getClass().getClass().getName() = " + user1.getClass().getClass().getName());
    }

}


















