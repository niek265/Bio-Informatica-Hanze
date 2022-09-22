# Language basics

## Learning outcomes
* Working with IntelliJ 
* Create and run JUnit tests
* Getting to know Java coding conventions 
* Basic OO programming

## Assignments 

1. In class `LanguageBasics`, work your way through the methods (from top to bottom) and implement them according to the instructions 
stated within the methods' Javadoc and/or in the method body.  
Don't forget to replace the `return 0;` or `return null;` statements with your calculated values! 
The tests are found in `/src/test/java/section1_intro/part1_language_basics/LanguageBasicsTest.java`. 
Again, if you want to run a method yourself, you can add a `main()` method.

2. Class `Point` has a method that is not implemented: `Point createInversePoint()`. This is your task. See its Javadoc for details. Run the test method `testCreateInversePoint()` in class `PointTest` to see if your solution is correct.

3. Class `Point` has a method that is not implemented: `double euclideanDistanceTo(Point otherPoint)`. This is your task. Run the test methods in class `PointTest` to see if your solution is correct.

4. Create a `main()` method demonstrating the use of class Point and its methods. (No JUnit test available)

5. Class `Rectangle` has a method that is not implemented: `int getSurface()`. This is your task. Test class `RectangleTest` can verify your solution.

6. Class `GeometryAnalyser` already has a `main()` method but without any code in it. 
You need to give it an implementation so that it can deal with command-line arguments.
Command-line arguments will be passed to the `main()` method as the `String[] args` argument (a String array). 
Assume you will receive a series of four numbers; two pairs, each representing the `x` and `y` value of a `Point` instance.  
The fifth and last argument should be either "dist" or "surf", indicating the desired operation. 
For example, if the application is run with `2 5 6 2 surf` it means the user wants the 
surface of the rectangle formed by `Point(2, 5)` (upperleft) and `Point(6, 2)` (lowerright) and the program output should simply state "12" (without the quotes). 
The option "dist" should work in a similar fashion: give the distance between the two points, but also round the result to 1 decimal.
Note that the "real" functionality has already been implemented in the previous assignments - don't repeat or copy that!
Class `GeometryAnalyserTest` will tell you if you're right.

See the post "Basic Program Design" (Part 1) for instructions on creating and modifying run 
configurations in IntelliJ, and to pass arguments to `main()`.

Some technical tips:   

- To perform String comparisons, use `stringOne.equals("stringTwo")`.
- To convert a String to an Integer, use `Integer.parseInt(String)`. Command-line arguments are in a String array, so any numeric values will need to be converted.
- To round a number, use `NumberFormat`. Here is an example:  
    
```java
NumberFormat numberFormat = NumberFormat.getNumberInstance();
numberFormat.setMaximumFractionDigits(1);
System.out.println(numberFormat.format(3.354)); //prints "3,6" in a Dutch Locale
```   

**_Challenge_**. With option "surf", if x1 < x2 or y1 < y2, the program should print "Illegal input" using `System.err()` and quit.

