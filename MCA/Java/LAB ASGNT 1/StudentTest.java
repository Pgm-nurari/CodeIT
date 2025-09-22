import java.util.Scanner;

class Student {
    String name;
    int rollNo;
    double marks;

    void acceptDetails(Scanner sc) {
        System.out.print("Name: ");
        name = sc.nextLine();
        System.out.print("Roll No: ");
        rollNo = Integer.parseInt(sc.nextLine());
        System.out.print("Marks: ");
        marks = Double.parseDouble(sc.nextLine());
    }

    void displayDetails() {
        System.out.println("Name: " + name + ", Roll No: " + rollNo + ", Marks: " + marks);
    }

    boolean checkPass() {
        return marks > 40.0;
    }
}

public class StudentTest {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Student[] s = new Student[3];
        for (int i = 0; i < 3; i++) {
            s[i] = new Student();
            System.out.println("Enter details for student " + (i + 1) + ":");
            s[i].acceptDetails(sc);
        }
        for (Student st : s) {
            st.displayDetails();
            System.out.println("Pass: " + st.checkPass());
        }
        sc.close();
    }
}