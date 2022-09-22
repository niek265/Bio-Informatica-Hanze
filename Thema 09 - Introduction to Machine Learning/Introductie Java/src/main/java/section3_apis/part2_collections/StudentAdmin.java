package section3_apis.part2_collections;

import java.util.List;
import java.util.Map;

/**
 * YOUR CHALLENGE:
 * This class only contains a so-called public API. There is no underlying code that supports the API.
 * It is your task to implement this logic. Using the right collection type(s).
 */
public class StudentAdmin {

    /**
     * Returns the students that are present in the database.
     * If the searchString is * (a wildcard), all students will be returned. Else,
     * a simple case insensitive substring match to both first name and family name will be performed.
     * @param searchString the substring string to look for
     * @return students
     */
    public List<Student> getStudents(String searchString) {
        //YOUR CODE HERE (and remove the throw statement)
        throw new UnsupportedOperationException("Not implemented yet");    }

    /**
     * Returns the grade of a student for the given course
     * @param student the student
     * @param course the course
     * @return grade
     */
    public double getGrade(Student student, Course course) {
        //YOUR CODE HERE (and remove the throw statement)
        throw new UnsupportedOperationException("Not implemented yet");
    }

    /**
     * returns all grades for a student, as [key=CourseID]:[value=Grade] Map
     * @param student the student to fetch grades for
     * @return grades
     */
    public Map<String, Double> getGradesForStudent(Student student) {
        //YOUR CODE HERE (and remove the throw statement)
        throw new UnsupportedOperationException("Not implemented yet");
    }

    /**
     * Returns all grades for a course, as [key=Student]:[value=Grade] Map
     * @param course the course
     * @return grades
     */
    public Map<Student, Double> getGradesForCourse(Course course) {
        //YOUR CODE HERE (and remove the throw statement)
        throw new UnsupportedOperationException("Not implemented yet");
    }
}
