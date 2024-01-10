import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Menu:\n1. Spaghetti Bolognese - Php 88.00\n2. Margherita Pizza - Php 320.00\n3. Caesar Salad - Php 77.00\n4. Grilled Chicken Sandwich - Php 85.00\n5. Chocolate Brownie - Php 40.00");
        System.out.println("Enter the item codes for the dishes you want to order (0 to finish):");

        double totalCost = 0;
        while (true) {
            int itemCode = scanner.nextInt();
            if (itemCode == 0) {
                break;
            }

            switch (itemCode) {
                case 1:
                    totalCost += 88.00;
                    System.out.println("Added Spaghetti Bolognese to your order.");
                    break;
                case 2:
                    totalCost += 320.00;
                    System.out.println("Added Margherita Pizza to your order.");
                    break;
                case 3:
                    totalCost += 77.00;
                    System.out.println("Added Caesar Salad to your order.");
                    break;
                case 4:
                    totalCost += 85.00;
                    System.out.println("Added Grilled Chicken Sandwich to your order.");
                    break;
                case 5:
                    totalCost += 40.00;
                    System.out.println("Added Chocolate Brownie to your order.");
                    break;
                default:
                    System.out.println("Invalid item code. Please enter a valid item code.");
            }
        }

        System.out.println("Total cost of your order: Php " + totalCost);
    }
}