import java.util.Scanner;

public class ArabellaCaesarCipher {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter a message to encrypt");
        StringBuilder message = new StringBuilder();
        String line;
        while (!(line = sc.nextLine()).equals(".")) {
            message.append(line).append("\n");
        }

        System.out.print("Enter the shift value for the message: ");
        int shift = sc.nextInt();

        long startTime = System.currentTimeMillis();
        String encryptedMessage = encrypt(message.toString(), shift);
        long endTime = System.currentTimeMillis();

        System.out.println("Encrypted message: " + encryptedMessage);
        System.out.println("Encryption time: " + "(endTime - startTime)" + " milliseconds");

        sc.close();
    }

    public static String encrypt(String message, int shift) {
        StringBuilder encryptedMessage = new StringBuilder();

        for (int i = 0; i < message.length(); i++) {
            char c = message.charAt(i);

            if (Character.isLetter(c)) {
                if (Character.isUpperCase(c)) {
                    c = (char) ((c - 'A' + shift + 26) % 26 + 'A');
                } else {
                    c = (char) ((c - 'a' + shift + 26) % 26 + 'a');
                }
            }

            encryptedMessage.append(c);

            try {
                Thread.sleep(1); // Add a delay of 20 milliseconds
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        return encryptedMessage.toString();
    }
}