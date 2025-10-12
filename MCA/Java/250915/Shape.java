public class Shape {

    // Area of Triangle
    double area(double base, double height) {
        return 0.5 * base * height;
    }

    // Area of Rectangle
    double area(int length, int breadth) {
        return length * breadth;
    }

    // Area of Circle
    double area(double radius) {
        return 3.14 * radius * radius;
    }

    // Area of Square
    int area(int side) {
        return side * side;
    }

    public static void main(String[] args) {
        Shape shape = new Shape();

        System.out.println("Area of Triangle: " + shape.area(10.0, 5.0));
        System.out.println("Area of Rectangle: " + shape.area(8, 6));
        System.out.println("Area of Circle: " + shape.area(4.5));
        System.out.println("Area of Square: " + shape.area(5));
    }
}
