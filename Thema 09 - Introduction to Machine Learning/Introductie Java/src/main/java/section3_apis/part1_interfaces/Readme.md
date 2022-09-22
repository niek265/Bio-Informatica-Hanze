# Interfaces

## Learning outcomes
* Getting to know interfaces 
* Implementing logic
* char to int conversions


## Assignment 1

This package contains an interface called `StringCombiner` that defines the contract for a single method: 
`String combine(String first, String second)`.

Another class in this package is `CombinerFactory` which has three so-called **_factory methods_**. A factory method is a 
 method that serves instances of a particular type (class or interface), where the exact implementation type (class) is not known.
Here, each factory method is supposed to serve a `StringCombiner` implementation. 

It is your task to create the described implementers according to the Javadoc comments of the three methods.  
There are several equally valid possibilities to solve this:  

- a regular class that implements the interface
- an anonymous local inner class
- an (anonymous) member (i.e. non-local) inner class.

Have a look at the post "Inner classes" (Part 4) if you are interested in the last two options.

The JUnit tests will tell you if the solutions are OK.

## Assignment 2

This package also contains the interface `EncryptionEngine` with two defined method signatures: `encrypt()` and `decrypt()`.
You have to create EncryptionEngine implementations in which the `decrypt()` call reverses the `encrypt()` result. 

1. **Encryption system one**: The Caesar cypher (see [wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)). There are many ways to do this.
Note you can treat the `char` type as if it is an `int`, as demonstrated by `character -= 3;`. Also noteworthy is the availability of methods `string.toCharArray()`, `Character.isUpperCase(character)` and `Character.isLowerCase(character)`

2. **Encryption system two**: Design and implement your own encryption logic. There are no tests for this, of course. 
