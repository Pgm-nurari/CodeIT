import java.util.Scanner;

class Employee {
    int empID;
    String empName;
    double salary;

    void getEmpData(Scanner sc) {
        System.out.print("EmpID: ");
        empID = sc.nextInt();
        sc.nextLine();
        System.out.print("EmpName: ");
        empName = sc.nextLine();
        System.out.print("Salary: ");
        salary = sc.nextDouble();
    }

    void printEmpData() {
        System.out.println("ID: " + empID + ", Name: " + empName + ", Salary: " + salary);
    }
}

public class EmployeeArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("How many employees? ");
        int n = sc.nextInt();
        Employee[] emps = new Employee[n];
        for (int i = 0; i < n; i++) {
            emps[i] = new Employee();
            System.out.println("Enter details for employee " + (i + 1));
            emps[i].getEmpData(sc);
        }
        System.out.println("Employee details:");
        for (Employee e : emps)
            e.printEmpData();
        sc.close();
    }
}