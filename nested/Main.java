import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter exam score:");
        int examScore = scanner.nextInt();
        System.out.println("Enter assignment score:");
        int assignmentScore = scanner.nextInt();
        System.out.println("Enter attendance percentage:");
        int attendance = scanner.nextInt();

        if (examScore < 0 || examScore > 100 || assignmentScore < 0 || assignmentScore > 50 || attendance < 0 || attendance > 100) {
            System.out.println("Invalid input. Please enter scores and attendance within the valid range.");
            return;
        }

        if (examScore >= 70 && assignmentScore >= 30 && attendance >= 75) {
            System.out.println("Congratulations! You passed with an A grade.");
        } else if (examScore >= 60 && assignmentScore >= 25 && attendance >= 70) {
            System.out.println("Congratulations! You passed with a B grade.");
        } else if (examScore >= 50 && assignmentScore >= 20 && attendance >= 65) {
            System.out.println("Congratulations! You passed with a C grade.");
        } else {
            System.out.println("Sorry, you did not pass.");
        }
    }
}