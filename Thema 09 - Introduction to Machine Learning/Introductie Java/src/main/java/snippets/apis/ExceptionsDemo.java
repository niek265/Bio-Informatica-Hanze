package snippets.apis;

public class ExceptionsDemo {
    public static void main(String[] args) {
        doFirst();
        try {
            thirdMethod();
        } catch (OutOfMemoryError error) {
            //recover from an out of memory error?
        }
    }

    private static void thirdMethod() {
    }

    private static void doFirst() {
        doSecond();
    }

    private static void doSecond() {
        int x = 42 / 0;
    }
}
