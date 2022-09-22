# Java data types

## Learning outcomes
* getting to know arrays
* basic programming (with `for`)
* Object-oriented design

## Assignments

This assignment is partly for you to implement and learn about types and partly as a demonstration of what Object Oriented code looks like in Java, with some xommonly used coding techniques and principles. Don't worry if you don't get it all at once; we'll discuss it in class as well.  

- This package contains a two-class program that can be used to process zoo information and print a zoo summary.
- There are two classes involved: `ZooApp` and `ZooSpecies`. Class `ZooSpecies` has been implemented completely. Study it carefully. This class demonstrates quite a few coding patterns that are common in Java - don't skip that! The Javadoc code comments explain. 
- The second class is `ZooApp`. It is the **_controller_** of the application, and it is the "main class" as well: it has the `main()` method that is required for an executable application. Within this class there are a few (parts of) methods that you should implement. Just follow the steps below.

1. The `main()` method receives from the command line and array: `String[] args`. The array should have this format (space-separated values): 
`Bonobo Giraffe Lion Lion Chimpanzee Giraffe`. Create a **_run configuration_**  that will pass such a value to main when the app is run (this has been shown in the first chapter).

2. The `main()` method creates and instance of `ZooApp` and passes the `args` array to the method `processZooData()`. 
Within this method you should process the command line arguments. Note that class `ZooSpecies` does most of the work; don't implement anything that is already there!

3. Method `printZooSummary()` is already partly implemented. It should print a species summary that looks like this:

```
The zoo has 4 species.
These are the species counts:
    Bonobo: 1
    Chimpanzee: 1
    Lion: 2
    Giraffe: 2
```

There is only a test for `processZooData()`.

- Hint: To find out which methods are available on an object, type the variable and a dot and IntelliJ will give suggestions. Typing F1 or Ctrl + Q will give more details on a method.
- Hint: To find out which method are available on a class, type the class name and a dot and IntelliJ will give suggestions.
- Hint: have a look at the String class on how to split strings into elements. Besides the help within IntelliJ you can also have a look at the [online docs](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html).
tool