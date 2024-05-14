/* @author: Dan Arnaiz
*/

public class BubbleSort {
    public static void main(String[] args) {
        int[] sampleArray = {64, 34, 25, 12, 22, 11, 90};
        bubbleSort(sampleArray);
        System.out.println("Sorted array:");
        for (int value : sampleArray) {
            System.out.print(value + " ");
        }
    }

    static void bubbleSort(int[] arr) {
        boolean swapped;
        for (int i = 0; i < arr.length - 1; i++) {
            swapped = false;
            for (int j = 0; j < arr.length - i - 1; j++) {
                // Unique part: Using bitwise XOR to swap without a temporary variable
                if (arr[j] > arr[j + 1]) {
                    arr[j] = arr[j] ^ arr[j + 1];
                    arr[j + 1] = arr[j] ^ arr[j + 1];
                    arr[j] = arr[j] ^ arr[j + 1];
                    swapped = true;
                }
            }
            // If no two elements were swapped by inner loop, then break
            if (!swapped)
                break;
        }
    }
}