package snippets.testtube3;

public class Bacterium extends Cell{
    private static int bacterialInitialDiameter = 10;
    private static final int growthIncrement = 1;
    private static final int maximumDiameter = 30;

    protected Bacterium() {
        super(bacterialInitialDiameter);
    }

    @Override
    public Cell grow() {
        setDiameter(getDiameter() + growthIncrement);
        if (getDiameter() > maximumDiameter) {
            return new Bacterium();
        } else {
            return null;
        }
    }
}