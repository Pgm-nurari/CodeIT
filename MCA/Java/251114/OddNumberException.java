public class OddNumberException {

    // Method to check number and throw exception if odd
    public static void checkEven(int number) {
        if (number % 2 != 0) {
            throw new IllegalArgumentException("The number " + number + " is odd.");
        } else {
            System.out.println("The number " + number + " is even. No exception.");
        }
    }

    public static void main(String[] args) {
        // Test case 1: Even number
        try {
            checkEven(10);
        } catch (IllegalArgumentException e) {
            System.out.println("Caught exception: " + e.getMessage());
        }

        // Test case 2: Odd number
        try {
            checkEven(7);
        } catch (IllegalArgumentException e) {
            System.out.println("Caught exception: " + e.getMessage());
        }
    }
}