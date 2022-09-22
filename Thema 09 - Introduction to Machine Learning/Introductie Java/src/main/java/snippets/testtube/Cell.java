package snippets.testtube;

public class Cell {
    public int diameter = 5;
    public int growthIncrement = 1;

    /**
     * Lets this cell grow in a single increment
     */
    public void grow() {
        //grow by 1 micrometer
        this.diameter += growthIncrement;
        System.out.println("I am a Bacterium. My size is " + this.diameter);
    }
}