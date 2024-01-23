import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String[][] students = {
            {"Henchie", "Hechona", "1/24/2001", "Bangkal, Davao City"},
            {"Dan", "Arnaiz", "1/30/2003", "Los Amigos, Davao City"},
            {"Danilo", "Bacalso", "6/5/2001", "Bankerohan, Davao City"},
            {"Warner", "Abella", "2/18/2001", "Osaka, Japan"},
            {"Harold", "Cayan", "6/18/2001", "Green Meadows, Davao City"},
            {"Delmar", "Larida", "2/17/2001", "Ula, Davao City"},
            {"John", "Bacsal", "9/28/2001", "Ula, Davao City"},
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