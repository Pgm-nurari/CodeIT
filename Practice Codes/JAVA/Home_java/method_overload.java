import java.util.Scanner;
public class method_overload{
    static Scanner sc=new Scanner(System.in);
    static void test(){
        float sum=(float)(5.0+6.0);
        System.out.println("The sum is: "+sum);
    }    
    static float test(float a,float b){
        float sum=a+b;
        return sum;
    }
    static float test(int n){
        if(n==0){
            System.out.print("\nEnter two numbers: ");
            float a=sc.nextInt();
            float b=sc.nextInt();
            float s=a+b;
            return s;
        }
        else{ return (float)1;}
    }
    static int menu(){
        System.out.println("|----| FUNCTION OVERLOADING |----|");
        System.out.println("1. test()\n2. test(a,b)\n3. test(0)");
        System.out.print("\nChoose an option: ");
        int opt=sc.nextInt();
        return opt;        
    }

    public static void main(String args[]){
        boolean x=true;
        while (x==true){
            int ch=menu();
            switch (ch){
                case 1:
                    System.out.println("test() method without return type.");
                    test();break;
                case 2:
                    System.out.println("test(a,b) method with float return type and 2 parameters.");
                    System.out.print("\nEnter 2 numbers: ");
                    float m=sc.nextFloat();float n=sc.nextFloat();
                    System.out.println(test(m,n));
                    break;
                case 3:
                    System.out.println("test() method with float return type.");
                    System.out.println(test(0));
                    break;
                default:
                    System.out.println("Invalid choice...!");
            }
            System.out.print("\nDo you want to continue [y/n]: ");
            char a=sc.next().charAt(0);
            if (a=='y'){
                x=true;
            }
            else{x=false;}
        }
        sc.close();
    }
}
