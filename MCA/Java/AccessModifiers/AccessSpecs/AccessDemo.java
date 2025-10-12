import mypack.*;

class PrivateDemo{
    private String name;
    int id;

    void setName(String name){
        this.name = name;
        id = 001;
    }
    void getDetails(){
        System.out.println("The details are: " + name + " " + id );
    }
}

public class AccessDemo{
    public static void main(String[] args) {

        // private keyword demo
        PrivateDemo pd1 = new PrivateDemo();
        pd1.setName("Nurari");
        pd1.getDetails();
        
        // System.out.println("Name: " + pd1.name);

        
        // default keyword demo
        Demo d1 = new Demo();
        d1.demo();
        System.out.println("Value for x in this class is: " + d1.x);


        Hello h1 = new Hello();
        h1.printHello();
        // example of public
        h1.displayHello();


        // example of protected access
        h1.displayProt();
        h1.displayKey();

        MyDemo md1 = new MyDemo();
        System.out.println(md1.key);
    }
}