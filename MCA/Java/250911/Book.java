public class Book {
    // Instance variables
    String title;
    String author;
    double price;

    // Default constructor
    Book() {
        title = "Unknown";
        author = "Unknown";
        price = 0.0;
    }

    // Parameterized constructor (title, author)
    Book(String title, String author) {
        this.title = title;
        this.author = author;
        this.price = 0.0; // default price
    }

    // Parameterized constructor (title, author, price)
    Book(String title, String author, double price) {
        this.title = title;
        this.author = author;
        this.price = price;
    }

    // Method to display book details
    void displayDetails() {
        System.out.println("Title: " + title);
        System.out.println("Author: " + author);
        System.out.println("Price: " + price);
        System.out.println("--------------------------");
    }

    // Main method
    public static void main(String[] args) {
        // Using default constructor
        Book b1 = new Book();

        // Using 2-parameter constructor
        Book b2 = new Book("The Alchemist", "Paulo Coelho");

        // Using 3-parameter constructor
        Book b3 = new Book("Atomic Habits", "James Clear", 499.50);

        // Displaying all books
        b1.displayDetails();
        b2.displayDetails();
        b3.displayDetails();
    }
}

