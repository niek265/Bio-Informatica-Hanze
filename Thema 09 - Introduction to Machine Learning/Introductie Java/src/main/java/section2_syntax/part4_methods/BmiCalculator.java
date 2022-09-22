/*
 * Copyright (c) 2015 Michiel Noback [michiel.noback@gmail.com].
 * All rights reserved.
 */
package section2_syntax.part4_methods;

import java.util.Scanner;

/**
 *
 * @author michiel
 */
public class BmiCalculator {
    private Scanner keyboard = new Scanner(System.in);
    /**
     * The string messages to accompany BMI categories
     */
    public static final String[] MESSAGES = new String[]{
        "Ondergewicht",
        "Gezond gewicht",
        "Overgewicht",
        "Obesitas",
        "Morbide Obesitas"
    };

    /**
     * starting point of your application.
     *
     * @param args the CL args
     */
    public static void main(String[] args) {
        //implement top-level logic such as fetching user input and creating a feedback message to user
        BmiCalculator bc = new BmiCalculator();
        double userHeigth = bc.getUserHeight();
        double userWeight = bc.getUserWeight();
        double userBMI = bc.calculateBMI(userWeight, userHeigth);
        String label = bc.getMessage(userBMI);

        //YOUR CODE HERE
        //generate output to user
        
    }

    /**
     * fetches the height of the user.
     * @return height the height in meters
     */
    public double getUserHeight() {
        System.out.print("Please give your height, in meters (e.g. 1.84): ");
        String input = keyboard.nextLine();
        double height = 0;
        try {
            height = Double.parseDouble(input);
        } catch (NumberFormatException ex) {
            System.out.println("This is no number! aborting...");
            System.exit(0);
        }
        return height;
    }

    /**
     * fetches the height of the user.
     * @return height the height in meters
     */
    public double getUserWeight() {
        //YOUR CODE HERE (and remove the throw statement)
        throw new UnsupportedOperationException("Not implemented yet");
    }
    
    /**
     * Returns the BMI given a weight in kilograms and a height in meters.
     *
     * @param weight the weight in kilograms
     * @param height the height in meters
     * @return bmi the body mass index
     * @throws IllegalArgumentException when illegal (zero or below) values are
     * provided for weight and/or length
     */
    public double calculateBMI(double weight, double height) {
        if (weight <= 0 || height <= 0) {
            throw new IllegalArgumentException("Error: both weight and height should be above 0. Given: weight=" 
                    + weight + ", height=" + height);
        }
        //YOUR CODE HERE (and remove the throw statement)
        //Gewicht in kilogram / (Lengte in meter * Lengte in meter)
        throw new UnsupportedOperationException("Not implemented yet");
    }

    /**
     * Will return an appropriate String representation belonging to a given
     * BMI.
     *
     * BMI index Categorie &lt;18.5 Ondergewicht 18.5 - 25.0 Gezond gewicht 25.0
     * - 30.0 Overgewicht 30.0 - 40.0 Obesitas &gt;40 Morbide Obesitas
     *
     * @param bmi the BMI
     * @return message
     * @throws IllegalArgumentException when illegal (zero or below) BMI value
     * is provided
     */
    public String getMessage(double bmi) {
        //YOUR CODE HERE (and remove the throw statement)
        throw new UnsupportedOperationException("Not implemented yet");
    }
}
