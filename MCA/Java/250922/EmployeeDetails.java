/*
 * Write a java program which creates a class Person with the instance variable name and method getName() to return the name. 
 * The class should have a parameterised constructor which takes name as the argument and assign it in the instance variable. 
 * Derive a class Employee from the class Person and the derived class should have an instance variable id. 
 * The class should have a method getId() to return the id and a parameterised constructor which takes id and name as the parameters to assign the values in the corresponding instance variables of the classes using its constructors. 
 * Display the assigned values using the getName() and getId() methods.
 */

class Person {
    String name;

    public Person(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}

class Employee extends Person {
    int id;

    public Employee(int id, String name) {
        super(name);
        this.id = id;
    }

    public int getId() {
        return id;
    }
}

public class EmployeeDetails {
    public static void main(String[] args) {
        Employee employee = new Employee(101, "John Doe");

        System.out.println("Displaying Employee Details:");
        System.out.println("Name: " + employee.getName());
        System.out.println("ID: " + employee.getId());
    }
}