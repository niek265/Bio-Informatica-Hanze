package section1_intro.part1_language_basics;

public class LanguageBasics {

    /**
     * A method that determines whether x is a multiple of y.
     * The modulo operator '%' is excellent for this job.
     * @param x
     * @param y
     * @return multiple
     */
    public boolean isMultiple(int x, int y) {
        if (x % y == 0) {
            return true;
        }
        else {
            return false;
        }
    }

    /**
     * This method should return the travelled distance (in meters) for the given speed (km/h) and
     * elapsed time (minutes).
     *
     * @param speedInKmPerHour
     * @param elapsedTimeInMinutes
     * @return
     */
    public double getDistanceInMeters(double speedInKmPerHour, double elapsedTimeInMinutes) {
        return ((speedInKmPerHour * (elapsedTimeInMinutes/60))*1000);
    }

    /**
     * This method should return the cumulative sum of 1 to n.
     * So, when 4 is passed, it should return 1 + 2 + 3 + 4 = 10
     * The for-loop is already given but you should initialize i to a correct value
     * and add the algorithm logic
     * @param n
     * @return cumulative sum
     */
    public int getCumulativeSum(int n) {
        int z = 0;
        for (int i = 1; i < n+1; i++) {
            z += i;
        }
        return z;
    }

    /**
     * This method should return "number" to the power of "powerUp", where the absolute value (the - sign is removed if
     * present) is taken of "powerUp". Again, the Math class may come in handy.
     * @param number the number to power up
     * @param powerUp the power up value
     * @return number^absolute(powerUp)
     */
    public double getTheAbsolutePower(int number, int powerUp) {
        return Math.pow(number, Math.abs(powerUp));
    }

    /**
     * In the following methods, several variables are declared and initialized.
     * Only one of the variables is named according to Java naming style rules.
     * Return the one that is correctly named (the value of the variable is irrelevant!).
     * @return correctVariable
     */
    public String returnCorrectlyNamedVariable_1() {
        String NameOfKing = "Willem Alexander";
        String name_of_king = "George IV";
        String nameOfKing = "Louis XIV, le Roi Soleil";
        String Name_Of_King = "Franz II";

        //return the correct variable
        return nameOfKing;
    }

    public String returnCorrectlyNamedVariable_2() {
        String score_board = "A";
        String ScoreBoard = "B";
        String score_Board = "C";
        String scoreBoard = "D";

        //return the correct variable
        return scoreBoard;
    }

    public String returnCorrectlyNamedVariable_3() {
        String DNAtranslator = "A";
        String dnaTranslator = "B";
        String DnaTranslator = "C";
        String DNA_translator = "D";

        //return the correct variable
        return dnaTranslator;
    }

}
