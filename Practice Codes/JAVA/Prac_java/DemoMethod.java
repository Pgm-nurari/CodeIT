// Class Method and an Instance Method.......

public class DemoMethod {
    static int stMem=20;

    public double calcAvg(int a, int b){ //Class Method...
        double s=(a+b)/2.0;
        return s;
    }
}

class testClass{
    public static int maximum(int a, int b){ //Instance Method...
        if (a>b)
            return a;
        else    
            return b;   
    }
    public static void main(String args[]) {
        DemoMethod obj1=new DemoMethod();
        int x=85;
        int y=26;
        int z=obj1.maximum(x,y);  //calling an instance method...
        System.out.println("The largest one is: "+z);
        double avg=obj1.calcAvg(x,y);  //Calling a class method...
        System.out.println("Average: " + avg);
        System.out.println("Static member has value: " + obj1.stMem);
    }        
}