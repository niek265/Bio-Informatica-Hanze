package snippets.apis;

import java.util.Arrays;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class RegexDemo {
    public static void main(String[] args) {
//        stringRegexDemo();
        patternMatcherDemo();
    }

    private static void patternMatcherDemo() {
        //case insensitive
        Pattern hinc2 = Pattern.compile("(?i)(GT([CT][AG])AC)");
        Matcher matcher = hinc2.matcher("GTCAACtgttgaccc");

        //is it present at the start?
//        System.out.println("matcher.lookingAt() = " + matcher.lookingAt());
        //does entire string match?
//        System.out.println("matcher.matches() = " + matcher.matches());

        while (matcher.find()) {
            System.out.println("matcher.group() = " + matcher.group());
            //whole pattern - same as group()
            System.out.println("matcher.group(0) = " + matcher.group(0));
            System.out.println("matcher.group(2) = " + matcher.group(2));
            System.out.println("matcher.start() = " + matcher.start());
        }

        //replace with group capture
        final String replaced = hinc2.matcher("GTCAACtgttgaccc").replaceAll("[[$1]]");
        System.out.println("replaced = " + replaced);
    }

    private static void stringRegexDemo() {
        String input = "Dogs rule this doggin' world";
        //replace() works with literal string!
        System.out.println(input.replace("[Dd]og", "Cat"));
        System.out.println(input.replace("Dog", "Cat"));
        //replaceAll() works with regex!
        System.out.println(input.replaceAll("[Dd]og", "Cat"));
        System.out.println(Arrays.toString(input.split("[Dd]")));
        //matches() looks at whole target string.
        System.out.println(input.matches("[Dd]ogs"));
        System.out.println(input.matches("^[Dd]ogs.+"));

        String INPUT = "This is the <title>example</title> "
                + "string which , I'm going to use for pattern matching .";

        // Split on whitespace stretches
        String[] splitString = (INPUT.split("\\s+"));

        // Removes whitespace between a word character and . or , using group references
        String pattern = "(\\w)(\\s+)([\\.,])";
        System.out.println(INPUT.replaceAll(pattern, "$1$3"));

        // Extract the text between the two title elements
        pattern = "(?i)(<title.*?>)(.+?)(</title>)";
        String updated = INPUT.replaceAll(pattern, "$2");
        System.out.println("updated = " + updated);


        String repeated = "ABCDEEEFGGHIJJJKL";
        System.out.println("ABCDEEEFGGHIJJJKL".replaceAll("(\\w)\\1+", "_rep_"));
        System.out.println("ABCDEEEFGGHIJJJKL".replaceAll("([A-Z]{3})\\1", "_rep_"));
    }


}
