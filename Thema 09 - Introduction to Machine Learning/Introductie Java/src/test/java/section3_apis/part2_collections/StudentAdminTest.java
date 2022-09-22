package section3_apis.part2_collections;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

class StudentAdminTest {
    private StudentAdmin studentAdmin;

    @BeforeEach
    void setupAdmin() {
        StudentAdminDataReader studentAdminDataReader = new StudentAdminDataReader();
        this.studentAdmin = studentAdminDataReader.importAll("data/students.txt", "data/courses.csv");
    }

    @Test
    void getStudentsAll() {
        final List<Student> students = studentAdmin.getStudents("*");
        assertEquals(20, students.size());
    }

    @Test
    void getStudentsWithEll() {
        //10767	Larae	Rowell
        //7330	Bulah	Kittrell
        List<Student> expected = List.of(
                new Student(10767, "Larae", "Rowell"),
                new Student(7330, "Bulah", "Kittrell"));
        final List<Student> actual = studentAdmin.getStudents("ell");
        assertEquals(2, actual.size());
        Set<Student> actualSet = new HashSet<>(actual);
        Set<Student> expectedSet = new HashSet<>(expected);

        assertTrue(expectedSet.equals(actualSet));
    }

    @Test
    void getStudentsWithFo() {
        //13038	Forrest	Southern
        //19085	Nola	Monfort
        List<Student> expected = List.of(
                new Student(13038, "Forrest", "Southern"),
                new Student(19085, "Nola", "Monfort"));
        final List<Student> actual = studentAdmin.getStudents("fo");
        assertEquals(2, actual.size());
        Set<Student> actualSet = new HashSet<>(actual);
        Set<Student> expectedSet = new HashSet<>(expected);

        assertTrue(expectedSet.equals(actualSet));
    }



    @Test
    void getGrade() {
        Student student = new Student(10767, "Larae", "Rowell");
        Course course = new Course("INTRO_JAVA");
        double actual = studentAdmin.getGrade(student, course);
        double expected = 9.384964365;
        assertEquals(expected, actual);

        student = new Student(19085, "Nola", "Monfort");
        course = new Course("APP_DESIGN");
        actual = studentAdmin.getGrade(student, course);
        expected = 9.537020454;
        assertEquals(expected, actual);

    }

    @Test
    void getGradesForStudent() {
        Student student = new Student(7330, "Bulah", "Kittrell");
        final Map<String, Double> expected = Map.of(
                "INTRO_JAVA", 8.27693365,
                "WIS1", 3.815038264,
                "APP_DESIGN",4.563326439);
        final Map<String, Double> actual = studentAdmin.getGradesForStudent(student);
        assertTrue(expected.equals(actual));
    }

    @Test
    void getGradesForCourse1() {
        Course course = new Course("INTRO_JAVA");
        final Map<Student, Double> actual = studentAdmin.getGradesForCourse(course);
        Student student = new Student(1846, "Collette", "Sommer");
        assertTrue(actual.containsKey(student));
        assertEquals(8.364090911, (double)actual.get(student));
    }

    @Test
    void getGradesForCourse2() {
        Course course = new Course("WIS1");
        final Map<Student, Double> actual = studentAdmin.getGradesForCourse(course);
        Student student = new Student(1846, "Collette", "Sommer");
        assertTrue(actual.containsKey(student));
        assertEquals(5.697041145, (double)actual.get(student));
    }
    /*
    Course ID;Student ID;Grade
    INTRO_JAVA;14154;7.480346167
    INTRO_JAVA;10767;9.384964365
    INTRO_JAVA;8062;5.635147227
    INTRO_JAVA;1921;6.282473118
    INTRO_JAVA;16358;5.338437627
    INTRO_JAVA;13038;7.430212271
    INTRO_JAVA;1846;8.364090911
    INTRO_JAVA;14117;4.370384218
    INTRO_JAVA;7330;8.27693365
    INTRO_JAVA;12431;4.075417445
    INTRO_JAVA;3009;4.718559939
    INTRO_JAVA;11307;5.675889829
    INTRO_JAVA;19085;5.930914505
    INTRO_JAVA;19205;7.038839406
    INTRO_JAVA;15335;5.130934811
    INTRO_JAVA;5385;5.896408514
    INTRO_JAVA;4216;6.581113314
    WIS1;14154;6.44801652
    WIS1;10767;5.729584253
    WIS1;8062;8.986842615
    WIS1;1921;7.286922235
    WIS1;16358;6.829401141
    WIS1;13038;6.500693744
    WIS1;1846;5.697041145
    WIS1;14117;5.851269644
    WIS1;7330;3.815038264
    WIS1;12431;4.845170962
    WIS1;3009;4.976768683
    WIS1;11307;7.627742847
    WIS1;19085;6.190065186
    WIS1;19205;8.498482407
    WIS1;15335;7.591321778
    WIS1;5385;7.853693273
    WIS2;4216;8.909742723
    APP_DESIGN;14154;2.950940702
    APP_DESIGN;10767;9.331852362
    APP_DESIGN;8062;6.789091362
    APP_DESIGN;1921;4.43800991
    APP_DESIGN;16358;5.002511803
    APP_DESIGN;13038;5.422729619
    APP_DESIGN;1846;4.527570952
    APP_DESIGN;14117;3.316937176
    APP_DESIGN;7330;4.563326439
    APP_DESIGN;12431;7.970253717
    APP_DESIGN;3009;3.341209357
    APP_DESIGN;11307;9.497751907
    APP_DESIGN;19085;9.537020454
    APP_DESIGN;19205;5.649364554
    APP_DESIGN;15335;6.431799567
    APP_DESIGN;5385;5.652499698
    */
    /*
        14154	Lawrence	Faw
        10767	Larae	Rowell
        8062	Cliff	Hassel
        1921	Alline	Peets
        16358	Kaitlyn	Leger
        13038	Forrest	Southern
        1846	Collette	Sommer
        14117	Shandra	Brame
        7330	Bulah	Kittrell
        12431	Bethann	Aguon
        3009	Mistie	Mazzeo
        11307	Cleo	Bontrager
        19085	Nola	Monfort
        19205	Rena	Decicco
        15335	Pei	Speirs
        5385	Reggie	Eatman
        4216	Ehtel	Veloz
        17554	Shizue	Naccarato
        32108	Randi	Mode
        55177	Deandra	Simmons
    **/
}