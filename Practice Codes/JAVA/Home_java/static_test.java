class test
{
    public static int count=0;

    test()
    {
        System.out.println("\ntest() constructor has been called.\n");
        count++;
    }
    void display()
    {
        System.out.println("Count of object is: "+count);
    }
}
public class static_test {
    public static void main(String arg[]){

        test obj1=new test();
        obj1.display();
        test.count--;
        test obj2=new test();
        obj2.display();
    }
}
