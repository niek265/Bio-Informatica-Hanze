package snippets.syntax;

public class MessageMaker {
    private final String name;
    private final int age;

    /**
     * Constructor makes it mandatory to instantiate with name and age arguments.
     * @param name the name
     * @param age the age
     */
    public MessageMaker(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void printMessage() {
        System.out.println("Hi " + name + ", your age is " + age);

        if(age < 18) {
            System.out.println("ahh the energy of youth");
        } else if (age < 50) {
            System.out.println("nice to meet somebody in the prime of their life!");
        } else {
            System.out.println("hey, don't worry - every day brings you closer to retirement");
        }
    }
}
