import java.util.Scanner;

public class Circle {
    static double pi = 3.14; // static variable

    double r; // radius
    Scanner scanObj = new Scanner(System.in);

    // Constructor
    Circle() {
        this.input();
    }

    void input() {
        System.out.print("Enter the radius: ");
        this.r = scanObj.nextDouble();
    }

    void Area() {
        double area = pi * Math.pow(r, 2);
        System.out.println("Area of the circle is: " + area);
    }

    void Circumference() {
        double circumference = 2 * pi * r;
        System.out.println("Circumference of the circle is: " + circumference);
    }

    public static void main(String[] args) {
        Circle c1 = new Circle();
        c1.Area();
        c1.Circumference();
    }
}

