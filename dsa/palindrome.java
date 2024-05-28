/*
 * Author: Dan Arnaiz
 * 
 */

import javax.swing.JOptionPane;
import java.util.Stack;

public class palindrome {
    public static void main(String[] args) {
        String input = JOptionPane.showInputDialog("Enter a string:");
        if (isPalindrome(input)) {
            JOptionPane.showMessageDialog(null, input + " is a palindrome.");
        } else {
            JOptionPane.showMessageDialog(null, input + " is not a palindrome.");
        }
    }

    public static boolean isPalindrome(String str) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < str.length(); i++) {
            stack.push(str.charAt(i));
        }
        StringBuilder reversed = new StringBuilder(str.length());
        while (!stack.isEmpty()) {
            reversed.append(stack.pop());
        }
        return str.equals(reversed.toString());
    }
}