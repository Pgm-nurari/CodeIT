abstract class Shape{
    abstract double calculateArea();
    abstract void displayArea();
}

class Circle extends Shape{
    static double pi = 3.14;
    double radius;

    Circle(double radius){
        this.radius = radius;
    }

    @Override
    double calculateArea(){
        return (pi*Math.pow(radius,2)); 
    }

    @Override
    void displayArea(){
        System.out.println("Area of the circle is: " + calculateArea());
    }
}

class Square extends Shape{
    double side;

    Square(double side){
        this.side = side;
    }

    @Override
    double calculateArea(){
        return (Math.pow(side,2)); 
    }

    @Override
    void displayArea(){
        System.out.println("Area of the square is: " + calculateArea());
    }
}

class Rectangle extends Shape{
    double length;
    double breadth;

    Rectangle(double length, double breadth){
        this.breadth = breadth;
        this.length = length;
    }

    @Override
    double calculateArea(){
        return (length*breadth); 
    }

    @Override
    void displayArea(){
        System.out.println("Area of the rectangle is: " + calculateArea());
    }
}

public class AbstractClass {
    public static void main(String[] args) {
        // Shape s = new Shape(); Abstract class can not be instantiated.
        Shape s;

        s = new Circle(10);
        s.displayArea();

        s = new Square(1.1);
        s.displayArea();

        s = new Rectangle(1.76, 100.00);
        s.displayArea();
    }
}
