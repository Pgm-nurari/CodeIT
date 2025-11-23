import java.util.Scanner;

public class ArithmeticHandler {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Enter first number: ");
            int num1 = scanner.nextInt();

            System.out.print("Enter second number: ");
            int num2 = scanner.nextInt();

            // Safe operations
            System.out.println("Addition: " + (num1 + num2));
            System.out.println("Subtraction: " + (num1 - num2));
            System.out.println("Multiplication: " + (num1 * num2));

            // Operations prone to ArithmeticException
            System.out.println("Division: " + (num1 / num2));
            System.out.println("Modulus: " + (num1 % num2));

        } catch (ArithmeticException e) {
            System.out.println("Error: Cannot divide by zero! (" + e.getMessage() + ")");
        } catch (Exception e) {
            System.out.println("Error: Invalid input or other error occurred.");
        } finally {
            System.out.println("Execution complete. Cleaning up resources.");
            scanner.close();
        }
    }
}