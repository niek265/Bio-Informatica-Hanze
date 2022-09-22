package snippets.apis;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.text.MessageFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class FilesPathsDemo {
    public static void main(String[] args) {
        //pathsDemo();
        //filesDemo();
        parseEmployees();
    }


    private static List<Employee> parseEmployees() {
        String fileName = "/Users/michiel/IdeaProjects/JavaIntroProgrammingAssignments/data/empl_data.csv";
        Path path = Paths.get(fileName);
        List<Employee> employees = new ArrayList<>();
        try (BufferedReader br = Files.newBufferedReader(path)) {
            String line;
            int lineNumber = 0;

            while ((line = br.readLine()) != null) {
                lineNumber++;
                //skips first header line
                if (lineNumber == 1) continue;
                //split on tabs
                String[] elements = line.split("\t");
                String name = elements[0];
                //convert to int
                int age = Integer.parseInt(elements[1]);
                String function = elements[2];
                //convert to double
                double salary = Double.parseDouble(elements[3]) * 1000;

                Employee emp = new Employee(name, age, salary);
                System.out.println(emp);
                employees.add(emp);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return employees;
    }

    private static void filesDemo() {
        Path dataPath = Paths.get("/Users/michiel/Desktop/test.txt");

        //creates the file if it does not exist
        if(! Files.exists(dataPath)) {
            try {
                Files.createFile(dataPath);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        //write some data to it
        try (BufferedWriter writer = Files.newBufferedWriter(dataPath, StandardOpenOption.APPEND)) {
            writer.write("Hi there");
            writer.newLine();
            writer.write("Bye now");
            writer.newLine();
        } catch (IOException e) {
            e.printStackTrace();
        }

        //For convenience, wrap it into a printwriter
        try (PrintWriter writer = new PrintWriter(Files.newBufferedWriter(dataPath, StandardOpenOption.APPEND))) {
            writer.println("I'm back!");
            writer.format("%s is mijn voornaam en %s mijn achternaam", "Michiel", "Noback");
            writer.println(MessageFormat.format("{0} is mijn voornaam en {1} mijn achternaam", "Jan", "Jansen"));
        } catch (IOException e) {
            e.printStackTrace();
        }

        try(BufferedReader reader = Files.newBufferedReader(dataPath)) {
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println("line = " + Arrays.toString(line.split(" ")));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    private static void pathsDemo() {
        String fileName = "/Users/michiel/IdeaProjects/JavaIntroProgrammingAssignments/data/proteins.fa";
        
        Path path = Paths.get(fileName);

        System.out.println("path = " + path);
        System.out.println("path.getParent() = " + path.getParent());
        System.out.println("path.getRoot() = " + path.getRoot());
        System.out.println("path.subpath(0,3) = " + path.subpath(0, 3));
        System.out.println("path.getFileName() = " + path.getFileName());
        //convert to File object
        File file = path.toFile();


        System.out.println("Files.isReadable(path) = " + Files.isReadable(path));
        System.out.println("Files.isDirectory(path) = " + Files.isDirectory(path));
        try {
            Path copy = Paths.get("/Users/michiel/Desktop/test.fa");
            //delete if it already exists
            Files.deleteIfExists(copy);
            System.out.println("Files.copy() = " + Files.copy(path, copy));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }



}
