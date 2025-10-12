// Base class
class Animal {
    void makeSound() {
        System.out.println("Some generic animal sound");
    }
}

// Subclass Dog
class Dog extends Animal {
    @Override
    void makeSound() {
        System.out.println("Dog barks: Woof Woof!");
    }
}

// Subclass Cat
class Cat extends Animal {
    @Override
    void makeSound() {
        System.out.println("Cat meows: Meow Meow!");
    }
}

// Main class
public class AnimalSound {
    public static void main(String[] args) {
        Animal a; // Reference variable of type Animal

        // Dynamic Polymorphism - Dog object
        a = new Dog();
        a.makeSound();

        // Dynamic Polymorphism - Cat object
        a = new Cat();
        a.makeSound();
    }
}
