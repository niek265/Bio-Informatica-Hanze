package snippets.syntax;

/**
 * This is a Javadoc comment for the Duck class.
 * It describes what the class models and should be used for.
 * */
public class Duck {
    /**
     * This is a Javadoc comment for quack().
     * It should include tags for method arguments, exceptions and return types.
     * @param loudness the loudness of the quack.
     */
    public void quack(int loudness) {
        //single-line logic comment
        System.out.println("Quacking at level " + loudness);
        /*I can write a multiline block of
        * comment like this*/
    }
}