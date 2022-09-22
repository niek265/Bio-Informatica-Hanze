package snippets.syntax;

import snippets.testtube.Cell;

import java.util.Arrays;
import java.util.stream.IntStream;

public class ArrayDemo {
    public static void main(String[] args) {
        //create by specifying size - will contain zeros
        int[] numbers = new int[5];
        //create by specifying contents
        double[] scores = {2.1, 3.0, 4.5, 5.6};
        //create by specifying size - will contain nulls
        Cell[] cells1 = new Cell[6];
        //create by specifying contents
        Cell[] cells2 = {new Cell(), new Cell(), new Cell()};

        char[] chars = new char[3];
        System.out.println(chars[2]);

        byte[] bytes = new byte[3];
        System.out.println("bytes[2] = " + bytes[2]);

        System.out.println("bytes = " + Arrays.toString(bytes));

        int size = 10;
        Cell[] cells = new Cell[size];
        IntStream.range(0, size).forEach(n -> cells[n] = new Cell());
        System.out.println("cells = " + Arrays.toString(cells));


        //multidimensional
        final int sideLength = 5;
        int[][] scoreBoard = new int[sideLength][sideLength];
        for (int i = 0; i < sideLength ; i++) {
            for (int j = 0; j < sideLength; j++) {
                scoreBoard[i][j] = i*j;
            }
        }

        for (int i = 0; i < sideLength ; i++) {
            System.out.println(Arrays.toString(scoreBoard[i]));
        }

    }
}
