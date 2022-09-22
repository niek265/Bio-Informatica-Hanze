package snippets.testtube2;

public class Cell {
    private int diameterInMicrometers = 5;
    private final int growthIncrementInMicrometers;

    /**
     * Construct with diameter and growth increment, in micrometers.
     *
     * @param diameterInMicrometers diameter between 1 and 40 micrometers
     * @param growthIncrementInMicrometers growth increment between 1 and 5 micrometers
     * @throws IllegalArgumentException ex if one of the arguments is out of range
     */
    public Cell(int diameterInMicrometers, int growthIncrementInMicrometers) {
        if (diameterInMicrometers < 1
            || diameterInMicrometers > 41
            || growthIncrementInMicrometers < 1
            || growthIncrementInMicrometers > 6
        ) {
            throw new IllegalArgumentException("Bacterium size must start between 0 and 40 " +
                    "and growth increment between 0 and 5");
        }
        this.diameterInMicrometers = diameterInMicrometers;
        //growth increment can never be changed after construction
        this.growthIncrementInMicrometers = growthIncrementInMicrometers;
    }

    /**
     * Serves the read-only property diameter.
     * @return diameter in micrometers
     */
    public int getDiameterInMicrometers() {
        return diameterInMicrometers;
    }

    /**
     * Grows this cell in a single increment, increasing its size with one time
     * the growth increment.
     *
     */
    public void grow() {
        this.diameterInMicrometers += growthIncrementInMicrometers;
        if (this.diameterInMicrometers > 1000) throw new Error("TestTube will explode in 5 seconds");
    }
}