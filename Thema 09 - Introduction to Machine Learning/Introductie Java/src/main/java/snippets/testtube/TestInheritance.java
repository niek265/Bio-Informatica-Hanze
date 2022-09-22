package snippets.testtube;

public class TestInheritance {
    public static void main(String[] args) {
        Cell cell = new Cell();
        cell.grow();
        cell.grow();
        System.out.println("-----------");
        CancerCell cCell = new CancerCell();
        cCell.grow();
        cCell.grow();
        cCell.move();
    }
}
