import java.util.Scanner;

public class Book {
    String title;
    String author;
    double price;

    Book() {
        this.title = "Unknown";
        this.author = "Unknown";
        this.price = 0.0;
    }

    Book(String title, String author) {
        this.title = title;
        this.author = author;
        this.price = 0.0;
    }

    Book(String title, String author, double price) {
        this.title = title;
        this.author = author;
        this.price = price;
    }

    void print() {
        System.out.println("Title: " + title + ", Author: " + author + ", Price: " + price);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter title: ");
        String t = sc.nextLine();
        System.out.print("Enter author: ");
        String a = sc.nextLine();
        System.out.print("Enter price: ");
        double p = sc.nextDouble();
        Book b1 = new Book();
        Book b2 = new Book(t, a);
        Book b3 = new Book(t, a, p);
        System.out.println("Default book:");
        b1.print();
        System.out.println("Title+Author book:");
        b2.print();
        System.out.println("Full book:");
        b3.print();
        sc.close();
    }
}