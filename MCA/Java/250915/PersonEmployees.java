// Base class
class Person {
    String fname;
    String lname;

    // Method to set name
    void setName(String fname, String lname) {
        this.fname = fname;
        this.lname = lname;
    }
}

// Subclass
class Employee extends Person {

    // Method to get full name
    void getName() {
        System.out.println("Full Name: " + fname + " " + lname);
    }

    // Main method
    public static void main(String[] args) {
        Employee emp = new Employee();
        emp.setName("John", "Doe");
        emp.getName();
    }
}
