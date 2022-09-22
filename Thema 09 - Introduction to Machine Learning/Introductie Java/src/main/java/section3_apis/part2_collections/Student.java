package section3_apis.part2_collections;

import java.util.Objects;

public class Student {
    private int studentId;
    private String firstName;
    private String lastName;

    public Student(final int studentId, final String firstName, final String lastName) {
        this.studentId = studentId;
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public int getStudentId() {
        return this.studentId;
    }

    public String getFirstName() {
        return this.firstName;
    }

    public String getLastName() {
        return this.lastName;
    }

    @Override
    public String toString() {
        return "Student{" +
                "studentId=" + studentId +
                ", firstName='" + firstName + '\'' +
                ", lastName='" + lastName + '\'' +
                '}';
    }

    @Override
    public boolean equals(final Object o) {
        if (this == o) return true;
        if (o == null || this.getClass() != o.getClass()) return false;
        final Student student = (Student) o;
        return this.studentId == student.studentId;
    }

    @Override
    public int hashCode() {
        return Objects.hash(this.studentId);
    }
}
