// Parent class
class Animal {
    Animal() {
        System.out.println("Animal constructor called");
    }

    void display() {
        System.out.println("I am an Animal");
    }
}

// Child class
class Dog extends Animal {
    Dog() {
        super(); // Calls Animal() constructor
        System.out.println("Dog constructor called");
    }

    void show() {
        super.display(); // Calls parent class method
        System.out.println("I am a Dog");
    }

    public static void main(String[] args) {
        Dog d = new Dog();
        d.show();
    }
}
