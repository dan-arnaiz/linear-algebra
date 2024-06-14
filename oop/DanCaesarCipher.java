public class DanCaesarCipher {
    public static String caesarCipher(String text, int shift) throws InterruptedException {
        StringBuilder result = new StringBuilder();
        char ch;
        for (int i = 0; i < text.length(); i++) {
            if (Character.isUpperCase(text.charAt(i))) {
                ch = (char)(((int)text.charAt(i) + shift - 65) % 26 + 65);
            } else {
                ch = (char)(((int)text.charAt(i) + shift - 97) % 26 + 97);
            }
            result.append(ch);
            // Introduce a delay
            if (i % 100 == 0) { // Adjust this condition to control the frequency of the delay
                Thread.sleep(1); // Adjust this value to control the length of the delay
            }
        }
        return result.toString();
    }

    public static void main(String[] args) throws InterruptedException {
        String text = """
        In the quiet embrace of the night, where stars illuminate the vast expanse of the sky, celestial wonders dazzle with their eternal brilliance. Each twinkling light, a beacon in the darkness, casts its ethereal glow across the heavens, painting a canvas of shimmering constellations. The soft radiance of distant galaxies and nebulae creates a spectacle of cosmic beauty, captivating observers below. Amidst the silent tranquility, the stars stand as timeless symbols of hope and wonder, their luminous presence a reminder of the boundless mysteries that stretch beyond our earthly realm.
        """;
        int shift = 5000;
        System.out.println("Text  : " + text);
        System.out.println("Shift : " + shift);
        
        long startTime = System.currentTimeMillis();
        String cipherText = caesarCipher(text, shift);
        long endTime = System.currentTimeMillis();
        
        System.out.println("Cipher: " + cipherText);
        System.out.println("Encryption time: " + (endTime - startTime) + " milliseconds");
    }
}


Shift: 5000
Runtime: 31 milliseconds