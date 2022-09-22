package snippets.syntax;

import snippets.testtube.Cell;

public class JavaTypesDemo {
    public static void main(String[] args) {
        /* INTEGER counts the number of kills */
        int killCount = 42;

        /*BOOLEAN for yes/no variables; indicates alive status*/
        boolean alive = false;

        /*DOUBLE for floating point values; indicates the average number of kills per life cycle*/
        double killAverage = 10.55;

        /*CHARACTER for single letter values;
        stores mode of the game 'N'=No mercy 'S'= Sissy*/
        char playmode = 'N';


        /*STRING for text values; the name of the player*/
        String player = "ZZZZZombie";


        System.out.println("player =       " + player);
        System.out.println("alive =        " + alive);
        System.out.println("play mode =    " + playmode);
        System.out.println("kill count =   " + killCount);
        System.out.println("kill average = " + killAverage);
    }


    public void demoInitDeclare(){
        //LEGAL
        int killCount;
        killCount = 0;

        //ILLEGAL; not initialized
        int livesLived; //no compile error here
        //System.out.println("livesLived = " + livesLived); //but here!
    }


    public static void usingPrimitives() {
        int x = 10;
        int y = 20;
        int squareSurface = x * y;
        System.out.println("squareSurface = " + squareSurface);
        /*Use the Math class many numeric operations and constants.
        * Note that 10^2 is NOT 10 raised by power 2, but 10 XOR 2 (bitwise)*/
        double circleSurface = Math.PI * Math.pow((0.5 * x), 2);
        System.out.println("circleSurface = " + circleSurface);
        double division = (double)x / y;
        System.out.println("division = " + division);


        double ratio = 1.234;
        int intRatio = (int)ratio;


        char nucleotide = 'A';
        //allowed, because a char is an 16-bit int under water
        System.out.println(nucleotide * 10); //650
        System.out.println((char)(nucleotide + 5));


        boolean isAlive = true;
        //not allowed; although in some languages this works just fine
        //System.out.println("isAlive * 10 = " + isAlive * 10);

        String name = "Hank";
        //surprisingly, this is allowed; the int is automatically converted (not cast!) into a String
        System.out.println(name + 10); //Hank10

        //not allowed; the * operator does not support these two types as operands
        //System.out.println("name * 10 = " + name * 10);
    }


    public static void stringDemo(){
        String dnaOne = "AGAGGTCTAGCTGA";
        String dnaTwo = "GGTCTAGC";
        String dnaThree = "GGtctAGc";
        String dnaFour = dnaThree.toUpperCase();

        System.out.println("dnaOne - character at position 6 = " + dnaOne.charAt(5)); //T
        System.out.println("dnaOne contains dnaTwo" + dnaOne.contains(dnaTwo)); //true
        System.out.println("dnaTwo equals dnaThree, ignoring case " + dnaTwo.equalsIgnoreCase(dnaThree)); //true
        System.out.println("dnaOne starts with \"AGAGGT\" " + dnaOne.startsWith("AGAGGT")); //true
        System.out.println("dnaFour.toCharArray() = " + dnaFour.toCharArray()); //[C@6f3b5d16 but this changes: this is the reference value (the remote control endpoint)

        String dnaFive = new String("AGAGGTCTAGCTGA");
        String dnaSix = "AGAGGTCTAGCTGA";
        System.out.println("dnaOne equals dnaFive: " + dnaOne.equals(dnaFive));
        System.out.println("dnaOne == dnaFive: " + (dnaOne == dnaFive));
        System.out.println("dnaOne == dnaSix: " + (dnaOne == dnaSix));
    }


    public static void primitivePassingDemo() {
        int x = 42;
        System.out.println("x = " + x);
        changePrimitiveVariable(x);
        System.out.println("x = " + x);
    }

    public static void changePrimitiveVariable(int number) {
        System.out.println("number = " + number);
        number = 55;
        System.out.println("number = " + number);
    }

    public static void referencePassingDemo() {
        Cell cell = new Cell();
        System.out.println("cell.diameter = " + cell.diameter);
        changeReferenceVariable(cell);
        System.out.println("cell.diameter = " + cell.diameter);
    }

    public static void changeReferenceVariable(Cell theCell) {
        System.out.println("theCell.diameter = " + theCell.diameter);
        theCell.diameter = 12;
        System.out.println("theCell.diameter = " + theCell.diameter);
    }


    public static void stringPassingDemo() {
        String hello = "Hello World";
        System.out.println("hello = " + hello);
        changeStringVariable(hello);
        System.out.println("hello = " + hello);

    }

    public static void changeStringVariable(String message) {
        System.out.println("message = " + message);
        message = "Bye now!";
        System.out.println("message = " + message);
    }

    public static void nullValueDemo() {
        String nullString = null;
        //prints just fine!
        System.out.println("nullString = " + nullString);
        //NullPointerException
        nullString.charAt(0);
    }
}
