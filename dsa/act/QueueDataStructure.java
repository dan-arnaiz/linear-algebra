/*
 * Author: Dan Arnaiz
 */


import javax.swing.JOptionPane;
import java.util.LinkedList;
import java.util.Queue;

public class QueueDataStructure {
    public static void main(String[] args) {
        Queue<String> queue = new LinkedList<>();

        // Get input from user and add to the queue
        String input = JOptionPane.showInputDialog("Enter a series of numbers, separated by commas:");
        String[] numbers = input.split(",");
        for (String number : numbers) {
            queue.add(number.trim());
        }

        // Get the search value from the user
        String searchValue = JOptionPane.showInputDialog("Enter a number to search for:");

        // Search for the value in the queue
        int location = 0;
        boolean found = false;
        for (String number : queue) {
            location++;
            if (number.equals(searchValue)) {
                found = true;
                break;
            }
        }

        // Display the result
        if (found) {
            JOptionPane.showMessageDialog(null, "Value found at position " + location + ".");
        } else {
            JOptionPane.showMessageDialog(null, "Value not found.");
        }
    }
}