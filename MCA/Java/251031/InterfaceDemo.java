//31/10/2025
/*Interface : Keyword = Interface 
implements used for inheritance
Mulitple Inheriance is implemente through this
We can inherit one interface into another interface, We use the keyword EXTENDS
After Java 8 , we can have methods with body before it wasnt possible 

Here no concept of Constructors , but we can have var in interface
But that var has to be initialized 
These are considered as PUBLIC and FINAL

FINAL : 1. Used with Variables , Methods and Classes
Relevance : Stops the inheritance 

Only two types of Method define inside Interface:
default and static methods
    interfacename.method   
*/ 
interface MyInterface1
{
    void testing();
    //void hello();
    default void mymethod()
    {
        System.err.println("MyMethod");
    }
    static void mystaticmethod()
    {
        System.err.println("My Static Method");
    }
    // No Body , only abstract methods 
}
interface MyInterface2 extends MyInterface1
{
    void hello();
}
class MyClass implements MyInterface2 
{
    @Override
   public void testing()
    {
        System.err.println("Testing Method");
    }
    @Override
    public void hello()
    {
        System.err.println("Hello ");

    }
}
class interfaceDemo
{
    public static void main(String[] args) {
        MyClass mc1 = new MyClass();
        mc1.testing();
       // mc1.hello();
       //interfaceDemo id = new interfaceDemo();
       

        
    }
}