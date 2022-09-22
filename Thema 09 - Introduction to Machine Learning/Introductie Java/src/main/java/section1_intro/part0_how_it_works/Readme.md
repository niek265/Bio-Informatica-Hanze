# How it works


There are several methods shown in class `StartingJava` (file `StartingJava.java`). You are supposed to work through them from the top of the file to the bottom.

Study the [**_Javadoc_**](https://en.wikipedia.org/wiki/Javadoc) that accompanies each method and implement them according to the instructions given therein. 

Usually this means you must implement the method body. Don't forget to replace the `return 0;` or `return null;` statements with your calculated values! 

Most assignments have one or more corresponding test methods that can be used to verify the correctness of your solution. 
These are located in `/src/test/java/section1_intro/part0_how_it_works/StartingJavaTest.java`). 
They have the same name as the method your are working on with the word `test` prepended. 
So, `printHelloWorld()` can be verified using `testPrintHelloWorld()`.

During the lesson several ways of running and interpreting tests will be demonstrated. The simplest way to run a test is by clicking on the small green triangle in the editor margin next to the test method name.

If you want to run a method yourself, you can add a `main()` method by typing `psvm` and then pressing the Tab character. This will create a `main()` method.
Within `main()`, create an object of type `StartingJava` and call the method you wish to test. 
The snippet below demonstrates this for `printHelloWorld()`. 

```java
public static void main(String[] args) {
    StartingJava startingJava = new StartingJava();
    startingJava.printHelloWorld();
}
```

You can then run `main()` by pressing the small green rectangle in the code editor margin or via the keyboard shortcut `Ctrl + Shift + R` anywhere within the editor. 
