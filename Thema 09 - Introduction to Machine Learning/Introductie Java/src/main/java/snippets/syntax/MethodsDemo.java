package snippets.syntax;

import java.util.Arrays;

public class MethodsDemo {

    public static void main(String[] args) {
        StaticVsInstance.addIntsStatic(2, 5);
        //WILL NOT COMPILE: not called on an instance
        //addIntsInstance(3, 4);

        StaticVsInstance statInst = new StaticVsInstance();
        //both can be called on an instance
        StaticVsInstance.addIntsStatic(5, 3);
        statInst.addIntsStatic(5, 6);
        statInst.addIntsInstance(3, 7);



//        PowerUpper powerUpper = new PowerUpper();
//        System.out.println("4 ^ 2 = " + powerUpper.powerUp(4));
        //powerUpper.power = 3;
//        System.out.println("4 ^ 3 = " + powerUpper.powerUp(4));

        PowerUpper powerUpper = new PowerUpper();
        System.out.println("4 ^ 2 = " + powerUpper.powerUp(4));
        System.out.println("4 ^ 3 = " + powerUpper.powerUp(4, 3));
        System.out.println("4.0 ^ 3.0 = " + powerUpper.powerUp(4.0, 3.0));
        System.out.println("4.7 ^ 3.9 = " + powerUpper.powerUp(4.7, 3.9));

        MyDataClass myDataClass = new MyDataClass();
        System.out.println("myDataClass.x = " + myDataClass.x);
        workWithClass(myDataClass);
        System.out.println("myDataClass.x = " + myDataClass.x);


        System.out.println("doStatistics(1, 2, 3) = " + Arrays.toString(doStatistics(1, 2, 3)));
        System.out.println("doStatistics(1, 2, 3, 4) = " + Arrays.toString(doStatistics(1, 2, 3, 4)));

        System.out.println("doStatistics(1,2,5,6) = " + doStatisticsTheGoodWay(1, 2, 5, 6));
    }

    static class Statistics{
        int sum;
        double average;

    @Override
    public String toString() {
        return "Statistics{" +
                "sum=" + sum +
                ", average=" + average +
                '}';
    }
    }

    /**
     * Calculates the sum and average of a series of numbers and
     * returns this as an stats object
     * @param numbers
     * @return statistics
     */
    static Statistics doStatisticsTheGoodWay(int... numbers){
        int sum = 0;
        for (int n : numbers) sum += n;
        double average = (double)sum/numbers.length;
        Statistics statistics = new Statistics();
        statistics.sum = sum;
        statistics.average = average;
        return statistics;
    }


    /**
     * Calculates the sum and average of a series of numbers and
     * returns this as an array with the sum at index 0 and the average at index 1
     * @param numbers
     * @return statistics
     */
    static double[] doStatistics(int... numbers){
        int sum = 0;
        for (int n : numbers) sum += n;
        double average = (double)sum/numbers.length;
        double[] result = {(double)sum, average};
        return result;
    }


    static class MyDataClass {
        int x = 42;
    }

    static void workWithClass(MyDataClass myDataClass) {
        myDataClass.x++;
    }




    public void printWelcome (String name) {
        System.out.println("Hello, " + name + ", we hope you enjoy our app.");
    }

    static class PowerUpper {
        /**
         * returns x ^ 2
         */
        int powerUp(int x) {
            System.out.println("method A");
            return powerUp(x, 2);
        }

        /**
         * returns x ^ power
         */
        int powerUp(int x, int power) {
            System.out.println("method B");
            //THIS WILL CAUSE A STACK OVERFLOW
            //return powerUp(x, power);
            //OK
            return powerUp((double)x, (double)power);
        }

        /**
         * returns x ^ power from two doubles, but converts the result to int
         */
        int powerUp(double x, double power) {
            System.out.println("method C");
            return (int)Math.pow(x, power);
        }

        //this is not an overload! a different return type
        double powerUp(int x, double power) {
            System.out.println("method D");
            return Math.pow(x, power);
        }

        //WON'T COMPILE! is not an overload, but a redefenition of "int powerUp(double x, double power)"
//        double powerUp(double x, double power) {
//            return Math.pow(x, power);
//        }
    }

}
