/**
 * The package declaration; it defines the namespace of this class
 * */
package snippets.syntax;

/**
 * The blueprint for MostBasicApp instances
 * */
public class MostBasicApp {
    /**
     * This is a STATIC method, which means it is a class-level method and needs no object/instance to
     * be called.
     * The return type is "void": it does not return anything.
     * @param args the command-line arguments are passed here as string array
     */
    public static void main(String[] args) {
        for (String arg : args) {
            System.out.println("arg = " + arg);
        }

        /**
         * Use indexing to access array elements
         */
        String name = args[0];
        /**
         * Parse String into int
         */
        int age = Integer.parseInt(args[1]);

        /*Here, a first object is instantiated and its `start()` method is called.*/
        MessageMaker messageMaker = new MessageMaker(name, age);
        messageMaker.printMessage();
    }

}
