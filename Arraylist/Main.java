import java.util.ArrayList;
import java.util.Scanner;

class Student {
    String firstName;
    String lastName;
    String dob;
    String address;

    Student(String firstName, String lastName, String dob, String address) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.dob = dob;
        this.address = address;
    }
}

class StudentManagementSystem {
    ArrayList<Student> students = new ArrayList<>();

    void addStudent(String firstName, String lastName, String dob, String address) {
        students.add(new Student(firstName, lastName, dob, address));
        System.out.println("<<<<<<<<<<<<<<<STUDENT ADDED SUCCESSFULLY>>>>>>>>>>>>>");
    }

    void updateStudent(String firstName, String newLastName, String newDob, String newAddress) {
        for (Student student : students) {
            if (student.firstName.equalsIgnoreCase(firstName)) {
                student.lastName = newLastName;
                student.dob = newDob;
                student.address = newAddress;
                System.out.println("<<<<<<<<<<<<<<<STUDENT UPDATED SUCCESSFULLY>>>>>>>>>>>>>");
                return;
            }
        }
        System.out.println("Student not found.");
    }

    void displayStudents() {
        for (Student student : students) {
            System.out.println(student.firstName + " " + student.lastName + " " + student.dob + " " + student.address);
        }
    }

    void searchStudent(String firstName) {
        for (Student student : students) {
            if (student.firstName.equalsIgnoreCase(firstName)) {
                System.out.println(student.firstName + " " + student.lastName + " " + student.dob + " " + student.address);
                return;
            }
        }
        System.out.println("Student not found.");
    }

    void removeStudent(String firstName) {
        students.removeIf(student -> student.firstName.equalsIgnoreCase(firstName));
        System.out.println("<<<<<<<<<<<<<<<STUDENT REMOVED SUCCESSFULLY>>>>>>>>>>>>>");
    }
}

public class Main {
    public static void main(String[] args) {
        StudentManagementSystem sms = new StudentManagementSystem();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("STUDENT MANAGEMENT SYSTEM MENU");
            System.out.println("1. Add Student");
            System.out.println("2. Update Students");
            System.out.println("3. Display Student List");
            System.out.println("4. Search Student");
            System.out.println("5. Remove Student");
            System.out.println("6. EXIT");
            System.out.println("Enter your Selection: ");
            int selection = scanner.nextInt();
            scanner.nextLine(); // consume newline

            if (selection == 1) {
                System.out.println("Enter Firstname: ");
                String firstName = scanner.nextLine();
                System.out.println("Enter Lastname: ");
                String lastName = scanner.nextLine();
                System.out.println("Date of Birth: ");
                String dob = scanner.nextLine();
                System.out.println("Address: ");
                String address = scanner.nextLine();
                sms.addStudent(firstName, lastName, dob, address);
            } else if (selection == 2) {
                System.out.println("Enter Firstname: ");
                String firstName = scanner.nextLine();
                System.out.println("Enter new Lastname: ");
                String newLastName = scanner.nextLine();
                System.out.println("Enter new Date of Birth: ");
                String newDob = scanner.nextLine();
                System.out.println("Enter new Address: ");
                String newAddress = scanner.nextLine();
                sms.updateStudent(firstName, newLastName, newDob, newAddress);
            } else if (selection == 3) {
                sms.displayStudents();
            } else if (selection == 4) {
                System.out.println("Enter Firstname: ");
                String firstName = scanner.nextLine();
                sms.searchStudent(firstName);
            } else if (selection == 5) {
                System.out.println("Enter Firstname: ");
                String firstName = scanner.nextLine();
                sms.removeStudent(firstName);
            } else if (selection == 6) {
                System.out.println("Exiting...");
                break;
            }
        }
    }
}