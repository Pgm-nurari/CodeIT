/*
Write a Java program to create a class called Animal with a method called makeSound(). 
Create a subclass called Dog that overrides the makeSound() method to bark. 
Invoke both methods using dynamic polymorphism.
*/
class Animal {
    public void makeSound() {
        System.out.println("The animal makes a sound.");
    }
}

class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("The dog barks.");
    }
}

public class AnimalSounds {
    public static void main(String[] args) {
        Animal genericAnimal = new Animal();
        Animal myDog = new Dog(); 

        System.out.println("Calling makeSound() on a generic Animal object:");
        genericAnimal.makeSound();

        System.out.println("\nCalling makeSound() on a Dog object referred by an Animal reference:");
        myDog.makeSound(); 
    }
}
