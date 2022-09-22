# Java Operators

## Learning outcomes
* getting to know Java operators and precedence
* getting to know classes and instances
* implementing algorithmic logic

## British Weight Units solver

This package contains two classes: `BritishWeightUnits` and `WeightUnitsSolver`. 
Class `BritishWeightUnits` is completely implemented; there is nothing to code there for you.

Class `WeightUnitsSolver` has a single method (`convertFromGrams(int grams)`) that should return a BritishWeightUnits instance
 representing the number of Pounds, Ounces, and Grams converted from a quantity expressed simply in (whole) Grams.
A pound is 454 grams and an ounce is 28 grams.
For example: 1000 grams is 2 pounds and 3 ounces and 8 grams
Tip: use the modulo (`%`) operator

You should also implement the error checking correctly - it is, for example, not possible to calculate from negative quantities. If the input is negative, an `IllegalArgumentException` should be thrown. 

You can `System.out.println()` instances of class `BritishWeightUnits`; the `toString()` method will be called. It will give output like this:

```
BritishUnitsCoins{pounds=2, ounces=3, grams=8}
```

As always, you are free to create a `main()` method for testing/development purposes.

You probably know where to find the tests by now.
