// Abstract class Employee
abstract class Employee {
    protected String name;
    protected double baseSalary;

    // Parameterized constructor
    public Employee(String name, double baseSalary) {
        this.name = name;
        this.baseSalary = baseSalary;
    }

    // Abstract methods
    abstract double calculateSalary();
    abstract void displayInfo();
}

// Manager subclass
class Manager extends Employee {
    private double bonus;

    public Manager(String name, double baseSalary, double bonus) {
        super(name, baseSalary);
        this.bonus = bonus;
    }

    @Override
    double calculateSalary() {
        return baseSalary + bonus;
    }

    @Override
    void displayInfo() {
        System.out.println("=== Manager Information ===");
        System.out.println("Name: " + name);
        System.out.println("Base Salary: " + baseSalary);
        System.out.println("Bonus: " + bonus);
        System.out.println("Total Salary: " + calculateSalary());
        System.out.println();
    }
}

// Programmer subclass
class Programmer extends Employee {
    private int overtimeHours;
    private double hourlyRate;

    public Programmer(String name, double baseSalary, int overtimeHours, double hourlyRate) {
        super(name, baseSalary);
        this.overtimeHours = overtimeHours;
        this.hourlyRate = hourlyRate;
    }

    @Override
    double calculateSalary() {
        return baseSalary + (overtimeHours * hourlyRate);
    }

    @Override
    void displayInfo() {
        System.out.println("=== Programmer Information ===");
        System.out.println("Name: " + name);
        System.out.println("Base Salary: " + baseSalary);
        System.out.println("Overtime Hours: " + overtimeHours);
        System.out.println("Hourly Rate: " + hourlyRate);
        System.out.println("Total Salary: " + calculateSalary());
        System.out.println();
    }
}

// Main class
public class EmployeeDemo {
    public static void main(String[] args) {
        Manager manager = new Manager("Alice", 50000, 10000);
        Programmer programmer = new Programmer("Bob", 40000, 20, 500);

        manager.displayInfo();
        programmer.displayInfo();
    }
}
