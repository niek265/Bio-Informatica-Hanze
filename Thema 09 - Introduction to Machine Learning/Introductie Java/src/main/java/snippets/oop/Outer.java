package snippets.oop;

//top level public class
public class Outer {
    //inner anonymous implementer of inner interface
    private Usable usable = new Usable() {
        public void use() {
            System.out.println("doing it this way");
        }
    };
    private Usable usableTwo = new Usable() {
        public void use() {
            System.out.println("doing it that way");
        }
    };
    //inner non-anonymous class instance
    private Usable usable3 = new UsableUsable();


    public static void main(String[] args) {
        Outer outer = new Outer();
        outer.usable.use();
        outer.usableTwo.use();
        outer.usable3.use();
        outer.useInners();
    }


    public void useInners() {
        Inner i = new Inner();
        i.doIt();
    }

    /* A non-static inner class that needs an instance of Outer to exist.
    * Usually it is extremely tightly bound to the Outer class logic*/
    private class Inner {
        public void doIt() {
            System.out.println("doing it inner");
            //access to instance fields!
            usableTwo.use();
        }
    }

    /*
    * A static (although not explicity stated) interface
     */
    private interface Usable {
        public void use();
    }

    /*static implementer*/
    private static class UsableUsable implements Usable {
        @Override
        public void use() {
            System.out.println("doing it the other way");
        }
    }
}

