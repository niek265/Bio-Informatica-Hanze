package snippets.syntax;

public class OperatorsDemo {
    public static void main(String[] args) {
        int x = 41;
        int count = 1;
        int y = x + ++count;
        System.out.println("count=" + count + "; y=" + y);

        x = 40;
        x %= 3;
        System.out.println("x = " + x);

        String name = "John Doe";
        name += (hasAcademicTitle() ? "PhD" : "");
    }

    private static boolean hasAcademicTitle() {
        return true;
    }

    public void instanceOfDemo() {
        Dog dog = new Dog();
        Wolf wolf = new Wolf();
        Chihuahua chihuahua = new Chihuahua();

        System.out.println("dog instanceof Animal = " + (dog instanceof Animal));
        System.out.println("dog instanceof Object = " + (dog instanceof Object));
        System.out.println("chihuahua instanceof Dog = " + (chihuahua instanceof Dog));
        System.out.println("chihuahua instanceof Animal = " + (chihuahua instanceof Animal));
        System.out.println("chihuahua instanceof Chihuahua = " + (chihuahua instanceof Chihuahua));
    }


    class Animal{}

    class Wolf extends Animal{}

    class Dog extends Animal{}

    class Chihuahua extends Dog{}
}
