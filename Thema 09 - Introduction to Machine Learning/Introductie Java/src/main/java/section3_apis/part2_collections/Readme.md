# Collections

## Learning outcomes
* Getting to know collection types 
* Processing and coupling data
* First encounter of encapsulation

## Assignment 

1. In this package you will find class `FindTheRightCollection`. 
It has a few methods that should all return a class - the class of the correct 
collection type. The Javadoc above the method describes what kind of usage should be best supported.
The first case is already implemented so you get the idea.
As usual, the JUnit tests will tell you if the solutions are OK.

2. In the `data` folder at the root of this project there are two data files: `students.txt` and `courses.csv`. 
These represent the students and their course results for three courses. 
In the current package four classes are already present: `Student`, `Course`, `StudentAdmin` and `StudentAdminDataReader`.  
 
- Class `Student` is completely implemented; you do not need to do anything there.   
- Class `Course` needs additional code to store the grades.  
- Class `StudentAdmin` only publishes its public API through method stubs, without any implementation. You will need to devise a data storage, and also supply method for adding stuff into it. 
- Finally, class `StudentAdminDataReader` contains the basic file reader functionality. Note the use of a dedicated interface to abstract away all common code in this class. Here, you will need to do some work as well.
    
**It is your task to implement all necessary code to support the public API correctly, using the correct collection types.**
You will need to implement a few methods in these three classes in order to achieve this.

I suggest these series of steps (although other routes are possible):

1. Implement `processLine()` in the inner class `StudentLineHandler` of `StudentAdminDataReader` to parse a student instance.
2. In class `StudentAdmin`, create an appropriate datastructure (Set, List, Map) to hold `Student` instances.
3. Pass the student instance from `StudentAdminDataReader` to class `StudentAdmin`, to a method that you will need to create (think which access modifier to use) and store it.
4. In class `StudentAdmin`, create an appropriate datastructure (Set, List, Map) to hold `Course` instances.
5. Implement `processLine()` in the inner class `CoursesLineHandler` of `StudentAdminDataReader` to parse a grade instance for each line. Pass this data to class `StudentAdmin`, to a method that you will need to create.
6. Modify class `Course` so it can store grades for students.
7. Within class `StudentAdmin`, process the course data. Create a new Course instance when required.
8. Now, finally, implement the public API (public methods) of class `StudentAdmin`.



To protect your data, it is never allowed to simply return the reference to a collection type via a getter. The concept is called **_encapsulation_** and violating it looks like this:

```java
package section3_apis.part2_collections;

import java.util.ArrayList;
import java.util.List;

public class StudentCollection {
    private List<Student> students = new ArrayList<>();
    
    public List<Student> getStudents() {
        /*DANGER! data encapsulion breached!*/
        return students;
    }
}
```

Much better and safer is this already:

```java
package section3_apis.part2_collections;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class StudentCollection {
    private List<Student> students = new ArrayList<>();

    public List<Student> getStudents() {
        /*Data is safe from external corruption*/
        return Collections.unmodifiableList(students);
    }
}
```

For largely this same reason, class `Student` has been implemented **_immutable_**. Have a look at this class and 
try to figure out the design aspects enforcing immutability.

The JUnit tests will tell you when you are finished.
