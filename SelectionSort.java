/* @author: Dan Arnaiz
*/

public class SelectionSort {
    public static void main(String[] args) {
        int[] sampleArray = {29, 72, 98, 13, 87, 66, 52};
        selectionSort(sampleArray);
        System.out.println("Sorted array:");
        for (int value : sampleArray) {
            System.out.print(value + " ");
        }
    }

    static void selectionSort(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            // Unique part: Using bitwise XOR for swapping without a temporary variable
            if (minIndex != i) {
                arr[i] = arr[i] ^ arr[minIndex];
                arr[minIndex] = arr[i] ^ arr[minIndex];
                arr[i] = arr[i] ^ arr[minIndex];
            }
        }
    }
}