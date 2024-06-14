import java.util.*;

public class KaryllCaesarCipher {
   
    // Method to normalize the shift value to be within the range of 0-25
    private static int normalizeShift(int shift) {
        return (shift % 26 + 26) % 26;
    }
 
    // Encryption method
    public static String encrypt(String message, int shift) {
        StringBuilder encryptedMessage = new StringBuilder();
        shift = normalizeShift(shift);
 
        for (char letter : message.toCharArray()) {
            if (Character.isUpperCase(letter)) {
                char encryptedChar = (char) (((letter - 'A' + shift) % 26) + 'A');
                encryptedMessage.append(encryptedChar);
            } else if (Character.isLowerCase(letter)) {
                char encryptedChar = (char) (((letter - 'a' + shift) % 26) + 'a');
                encryptedMessage.append(encryptedChar);
            } else {
                encryptedMessage.append(letter);
            }
        }
 
        return encryptedMessage.toString();
    }
   
    // Decryption method
    public static String decrypt(String message, int shift) {
        return encrypt(message, 26 - normalizeShift(shift));
    }
 
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        boolean continueProgram = true;
 
        while (continueProgram) {
            System.out.println("Enter the message that you want to ENCRYPT or DECRYPT: ");
            String message = input.nextLine();
 
            System.out.println("Enter the shift value: ");
            int shift = input.nextInt();
 
            input.nextLine(); // Consume the newline character
 
            System.out.println("What do you want to do with the message?");
            System.out.println("Click [1] to ENCRYPT the message.");
            System.out.println("Click [2] to DECRYPT the message.");
            String choice = input.nextLine();

            long startTime, endTime;
 
            if (choice.equals("1")) {
                startTime = System.currentTimeMillis();
                String encryptedMessage = encrypt(message, shift);
                endTime = System.currentTimeMillis();
                System.out.println("Encrypted Message: " + encryptedMessage);
                System.out.println("Encryption time: " + (endTime - startTime) + " milliseconds");
            } else if (choice.equals("2")) {
                startTime = System.currentTimeMillis();
                String decryptedMessage = decrypt(message, shift);
                endTime = System.currentTimeMillis();
                System.out.println("Decrypted Message: " + decryptedMessage);
                System.out.println("Decryption time: " + (endTime - startTime) + " milliseconds");
            } else {
                System.out.println("Invalid choice! Please enter '1' or '2'.");
            }
 
            boolean validInput = false;
            while (!validInput) {
                System.out.println("Do you want to continue? Click [Y] if Yes or [N] if No.");
                String continueChoice = input.nextLine().toUpperCase();
 
                if (continueChoice.equals("Y")) {
                    validInput = true;
                } else if (continueChoice.equals("N")) {
                    continueProgram = false;
                    validInput = true;
                } else {
                    System.out.println("Invalid input! Please enter 'Y' or 'N'.");
                }
            }
        }
       
        input.close();
        System.out.println("You are now exiting the program...");
    }
}
