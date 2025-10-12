// Parent class
class Vehicle {
    String brand;
    int year;

    // Parameterized constructor
    Vehicle(String brand, int year) {
        this.brand = brand;
        this.year = year;
    }

    void displayInfo() {
        System.out.println("Brand: " + brand);
        System.out.println("Year: " + year);
    }
}

// Child class
class Car extends Vehicle {
    String model;

    // Constructor with super()
    Car(String brand, int year, String model) {
        super(brand, year); // Calls Vehicle's parameterized constructor
        this.model = model;
    }

    void display() {
        super.displayInfo(); // Calls Vehicle's method
        System.out.println("Model: " + model);
    }

    public static void main(String[] args) {
        Car c = new Car("Toyota", 2024, "Fortuner");
        c.display();
    }
}

