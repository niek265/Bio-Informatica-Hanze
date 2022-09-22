# Creating a listing of all substrings of a string  #

## Learning outcomes ##
* getting to know Java syntax and types
* working with user input
* getting to know Java String class
* getting to know the Java *for* loop


## Assignment details ##

Class `AllSubstringsPrinter` contains two methods, one of which is `printSubstringsLeftAlignedLeftTruncated()`.
Given a String object, it should print all possible substrings of it where in each iteration 
 the rightmost character is left out.
 
For example, this method call:

```java
AllSubstringsPrinter allSubstringsPrinter = new AllSubstringsPrinter();
allSubstringsPrinter.printSubstringsLeftAlignedLeftTruncated("GATCG");
``` 

should generate the following output to console

```
GATCG
ATCG
TCG
CG
G
```

Once you have this method implemented, use the acquired knowledge to expand on this topic.

You have to implement method `printAllSubstrings()` that also generates (prints) all possible substrings, but accepts two 
additional arguments. The three arguments are    

- a String to substring
- a boolean indicating whether the String should be left-truncated or right-truncated (`true` for left truncated)
- a boolean indicating whether the String should be left-aligned or right-aligned (`true` for left-aligned)

For example, this method call:

```java
AllSubstringsPrinter allSubstringsPrinter = new AllSubstringsPrinter();
allSubstringsPrinter.printAllSubstrings("GATCG", true, true);
``` 

should print left truncated, left aligned and will generate the following output to console

```
GATCG
ATCG
TCG
CG
G
```

and this method call:

```Java
asp.printAllSubstrings("GATCG", true, false);
``` 

will generate the following output to console

```
GATCG
 ATCG
  TCG
   CG
    G
```

and this method call:

```Java
asp.printAllSubstrings("GATCG", false, true);
``` 

will generate the following output to console

```
GATCG
GATC
GAT
GA
G
```

There is a helper method present (`createSpacer()`) that you can use to create spacers of a given length.