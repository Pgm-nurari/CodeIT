class Book{
    String title;
    String author;
    Float price;

    Book(){
        title = "Brace Yourself";
        author = "Mr. Invisible";
        price = 2.0f;
    }
    Book(String new_title, String new_author){
        title = new_title;
        author = new_author;
        price = 2.0f;
    }
    Book(String new_title, String new_author, Float new_price){
        title = new_title;
        author = new_author;
        price = new_price;
    }

    void getDetails(){
        String result = String.format("Book Details:\nBook Name: %s\nBook Author: %s\nBook Price: %.2f", title, author, price);
        System.out.println(result);
    }
}

public class BookConstructor{
    public static void main(String[] args) {
        //Default Constructor...
        Book b1 = new Book();
        b1.getDetails();

        //Parameterized Constructor without price...
        Book b2 = new Book("Skill Issue", "Mrs. Alluviere");
        b2.getDetails();

        //Parameterized Constructor with price...
        Book b3 = new Book("Skill Issue", "Mrs. Alluviere", 99.95f);
        b3.getDetails();
    }
}