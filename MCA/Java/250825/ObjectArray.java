import java.util.Scanner;

class Employee {
    int empno;
    String empname;
    String designation;
    String department;
}

public class ObjectArray {
    public static void main(String[] Args) {
        Scanner input = new Scanner(System.in);

        // This creates an array of 5 null references
        Employee[] emp = new Employee[5];

        System.out.println("Enter details for 5 employees:");

        // Use a traditional for-loop for initialization
        for (int i = 0; i < emp.length; i++) {
            System.out.println("\nEnter details for employee " + (i + 1) + ":");

            // 1. Create a new Employee object and assign it to the array at index i
            emp[i] = new Employee();

            // 2. Populate the fields of the object in the array
            System.out.print("Enter the employee ID: ");
            emp[i].empno = input.nextInt();
            input.nextLine(); // Consume the leftover newline character

            System.out.print("Enter the employee Name: ");
            emp[i].empname = input.nextLine(); // Use nextLine() to read full names

            System.out.print("Enter the employee Designation: ");
            emp[i].designation = input.nextLine();

            System.out.print("Enter the employee Department: ");
            emp[i].department = input.nextLine();
        }

        System.out.println("\n--- Employee Details ---");
        // The enhanced for-loop is perfect for reading data
        for (Employee e : emp) {
            System.out.println("\nEmployee ID: " + e.empno);
            System.out.println("Employee Name: " + e.empname);
            System.out.println("Employee Designation: " + e.designation);
            System.out.println("Employee Department: " + e.department);
        }

        input.close(); // Good practice to close the scanner
    }
}