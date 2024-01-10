import java.util.*;
import java.io.*;

class Student {
    int id;
    String name;
    List<Integer> grades;

    Student(int id, String name, List<Integer> grades) {
        this.id = id;
        this.name = name;
        this.grades = grades;
    }
}

class GradeRecordManager {
    List<Student> students = new ArrayList<>();

    void inputGrades() throws IOException {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Enter student ID:");
    while (!scanner.hasNextInt()) {
        System.out.println("That's not a number! Please enter a valid student ID:");
        scanner.next();
    }
    int id = scanner.nextInt();
    System.out.println("Enter student name:");
    String name = scanner.next();
            if (grade == -1) {
                break;
            }
            grades.add(grade);
        }
        students.add(new Student(id, name, grades));
        saveToFile();
    }

    void retrieveGrades() throws IOException {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter student ID:");
        int id = scanner.nextInt();
        loadFromFile();
        for (Student student : students) {
            if (student.id == id) {
                System.out.println("Name: " + student.name);
                System.out.println("Grades: " + student.grades);
                return;
            }
        }
        System.out.println("No student found with ID " + id);
    }

    void saveToFile() throws IOException {
        try (PrintWriter out = new PrintWriter(new FileWriter("grade_records.txt"))) {
            for (Student student : students) {
                out.println(student.id);
                out.println(student.name);
                for (int grade : student.grades) {
                    out.println(grade);
                }
                out.println(-1);
            }
        }
    }

    void loadFromFile() throws IOException {
        students.clear();
        try (Scanner in = new Scanner(new FileReader("grade_records.txt"))) {
            while (in.hasNext()) {
                int id = in.nextInt();
                String name = in.next();
                List<Integer> grades = new ArrayList<>();
                while (true) {
                    int grade = in.nextInt();
                    if (grade == -1) {
                        break;
                    }
                    grades.add(grade);
                }
                students.add(new Student(id, name, grades));
            }
        }
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        GradeRecordManager manager = new GradeRecordManager();
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("1. Input grades\n2. Retrieve grades\n3. Exit");
            int choice = scanner.nextInt();
            if (choice == 1) {
                manager.inputGrades();
            } else if (choice == 2) {
                manager.retrieveGrades();
            } else {
                break;
            }
        }
    }
}