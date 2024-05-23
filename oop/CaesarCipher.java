/*author: @dan-arnaiz
 * 
 * 
 */


public class CaesarCipher {
    public static String caesarCipher(String text, int shift) {
        StringBuilder result = new StringBuilder();
        char ch;
        for (int i = 0; i < text.length(); i++) {
            if (Character.isUpperCase(text.charAt(i))) {
                ch = (char)(((int)text.charAt(i) + shift - 65) % 26 + 65);
            } else {
                ch = (char)(((int)text.charAt(i) + shift - 97) % 26 + 97);
            }
            result.append(ch);
        }
        return result.toString();
    }

    public static void main(String[] args) {
        String text = "HelloWorld";
        int shift = 3;
        System.out.println("Text  : " + text);
        System.out.println("Shift : " + shift);
        System.out.println("Cipher: " + caesarCipher(text, shift));
    }
}