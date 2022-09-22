package snippets.syntax;

public class StaticVsInstance {

    /**
     * class method
     */
    static int addIntsStatic(int x, int y) {
        return x + y;
    }

    /**
     * instance method
     */
    int addIntsInstance(int x, int y) {
        return x + y;
    }
}
