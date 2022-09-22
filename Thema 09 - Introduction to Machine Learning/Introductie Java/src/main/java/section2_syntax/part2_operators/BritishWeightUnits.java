/*
 * Copyright (c) 2015 Michiel Noback [michiel.noback@gmail.com].
 * All rights reserved.
 */

package section2_syntax.part2_operators;

/**
 * This class represents British Weight units as a combination of pounds, ounces and grams.
 * It is an _immutable_ class because after initialization its fields cannot be modified anymore externally.
 */
public class BritishWeightUnits {
    private final int pounds;
    private final int ounces;
    private final int grams;

    /**
     * Constructs with relevant quantities.
     * @param pounds the pounds quantity
     * @param ounces the ounces quantity
     * @param grams the grams quantity
     */
    public BritishWeightUnits(int pounds, int ounces, int grams) {
        this.pounds = pounds;
        this.ounces = ounces;
        this.grams = grams;
    }

    public int getPounds() {
        return pounds;
    }

    public int getOunces() {
        return ounces;
    }

    public int getGrams() {
        return grams;
    }

    /**
     * This method generates a string representation of instances of this class.
     * You get its output when you print them.
     * @return string representation
     */
    @Override
    public String toString() {
        return "BritishUnitsCoins{" + "pounds=" + pounds + ", ounces=" + ounces + ", grams=" + grams + '}';
    }
}
