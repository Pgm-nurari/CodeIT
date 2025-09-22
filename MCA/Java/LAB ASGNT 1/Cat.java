public class Cat {
    String name;
    int age;

    Cat() {
        name = "Unknown";
        age = 0;
    }

    void print() {
        System.out.println("Name: " + name + ", Age: " + age);
    }

    public static void main(String[] args) {
        Cat c = new Cat();
        c.print();
    }
}