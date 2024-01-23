import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String[][] students = {
            {"Henchie", "Hechona", "1/24/2001", "Bangkal, Davao City"},
            {"Dan", "Arnaiz", "1/24/2001", "Bangkal, Davao City"},
            {"Danilo", "Bacalso", "1/24/2001", "Bangkal, Davao City"},
            {"Warner", "Abella", "1/24/2001", "Bangkal, Davao City"},
            {"Harold", "Cayan", "1/24/2001", "Bangkal, Davao City"},
            {"Delmar", "Larida", "1/24/2001", "Bangkal, Davao City"},
            {"John", "Bacsal", "1/24/2001", "Bangkal, Davao City"},
        };

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter Firstname: ");
        String firstName = scanner.nextLine();

        for (String[] student : students) {
            if (student[0].equalsIgnoreCase(firstName)) {
                System.out.println("FullName: " + student[1] + ", " + student[0]);
                System.out.println("Date of Birth: " + student[2]);
                System.out.println("Address: " + student[3]);
                return;
            }
        }

        System.out.println("Student not found.");
    }
}