package snippets.testtube3;

public class Eukaryote extends Cell{
    private static int eukaryoteInitialDiameter = 20;
    private static final int growthIncrement = 3;
    private static final int maximumDiameter = 80;

    protected Eukaryote() {
        super(eukaryoteInitialDiameter);
    }

    @Override
    public Cell grow() {
        setDiameter(getDiameter() + growthIncrement);
        if (getDiameter() > maximumDiameter) {
            return new Eukaryote();
        } else {
            return null;
        }
    }
}
