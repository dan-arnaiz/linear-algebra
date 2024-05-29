/*
 * Author: Dan Arnaiz
 */


import javax.swing.JOptionPane;
import java.util.Stack;

public class StackDataStructure {
    public static void main(String[] args) {
        Stack<String> stack = new Stack<>();

        // Get input from user and push onto the stack
        String input = JOptionPane.showInputDialog("Enter a series of numbers, separated by commas:");
        String[] numbers = input.split(",");
        for (String number : numbers) {
            stack.push(number.trim());
        }

        // Create a new stack for the reversed order
        Stack<String> reversedStack = new Stack<>();
        for (String number : stack) {
            reversedStack.push(number);
        }

        // Build the reversed stack string
        StringBuilder reversedStackString = new StringBuilder();
        while (!reversedStack.isEmpty()) {
            reversedStackString.append(reversedStack.pop()).append(" ");
        }

        // Display the original and reversed stack in a single dialog
        JOptionPane.showMessageDialog(null, "Original Stack: " + stack + "\nReversed Stack: " + reversedStackString.toString().trim());
    }
}