package snippets.testtube3;

public abstract class Cell {
    //no decent defaults possible at level of class Cell,
    //but we know this field is relevant
    private int diameter;

    public Cell(int initialDiameter) {
        this.diameter = initialDiameter;
    }

    public int getDiameter() {
        return diameter;
    }

    protected void setDiameter(int newDiameter) {
        this.diameter = newDiameter;
    }

    public abstract Cell grow();

    public static Cell of(String type) {
        switch (type) {
            case "Bacteria": return new Bacterium();
            case "Eukarya": return new Eukaryote();
            default: throw new IllegalArgumentException("Unknown cell type: " + type);
            //room for more cell types - yes this can be improved as well
        }
    }
}
