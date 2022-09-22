# Exercises combining previous lesson material

## Learning outcomes
* getting to know Java syntax and types, in particular Array
* implementing algorithmic logic
* working with user input


## Assignment: BMI calculator
You will create functionality that calculates a BMI based on a user-provided weight and height.  
Also, you will need to convert this into an appropriate textual label (message).  
To achieve this goal you have to write implementations for the given method stubs in class `BmiCalculator`.
One method, `calculateBMI()`, can be used to calculate the BMI of a person by asking the user for their weight and height.  
The other, `getMessage()`, can be used to convert a BMI value into an appropriate textual label.  
  
The main() method is already implemented, making it possible to use this class as an actual program. 
There are several places that need your attention; they are indicated with `//YOUR CODE HERE`, usually followed by a 
`throw new UnsupportedOperationException("Not implemented yet");` statement.

The string labels are already provided for you. **You must use these**:

```Java
public static final String[] MESSAGES = new String[]{
    "Ondergewicht",
    "Gezond gewicht",
    "Overgewicht",
    "Obesitas",
    "Morbide Obesitas"
};
```

For this assignment you will need to get user input. 
In Java this can be achieved (amongst other means) by using the Scanner class 
to read from the console, like this:

```Java
Scanner keyboard = new Scanner(System.in);  
System.out.print("SAY SOMETHING: ");  
String input = keyboard.nextLine();  
System.out.println("INPUT=" + input);  
```

One of the methods (fetching user input for height) is already implemented for you as an example.

Of course, the Java Exception mechanism has not been dealt with in the course. 
Therefore, an example of its use is given in the method calculateBMI(), already providing you 
with two passed tests!
You can use this example to create the implementation of method getMessage().
