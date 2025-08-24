import java.util.Scanner;

public class method_cal {

    public static void sum(){
        System.out.print("\nEntar a number :");
        int a=sc.nextInt();
        System.out.print("\nEntar second number :");
        int b=sc.nextInt();        
        System.out.print("\nSum is:"+(a+b));
    }
    public static void sub(){
        System.out.print("\nEntar a number :");
        int a=sc.nextInt();
        System.out.print("\nEntar second number :");
        int b=sc.nextInt();        
        System.out.print("\nDifference is:"+(a-b));
    }
    public static void multiply(){
        System.out.print("\nEntar a number :");
        float a=sc.nextFloat();
        System.out.print("\nEntar second number :");
        float b=sc.nextFloat();        
        System.out.println("Result is:"+(a*b));
    }
    public static void divide(){
        System.out.print("\nEntar a number :");
        float a=sc.nextFloat();
        System.out.print("\nEntar second number :");
        float b=sc.nextFloat();        
        System.out.println("Result is:"+(a/b));
    }            


    static Scanner sc=new Scanner(System.in);
    public static int menu(){
        System.out.println("************");
        System.out.println("    MENU    ");
        System.out.println("************");
        System.out.println("1.ADD\n2.SUBTRACT\n3.MULTIPLY\n4.DIVIDE");
        System.out.println("\nEnter your choice :");
        int num=sc.nextInt();
        return num;
    }
    public static void main(String args[]){
        boolean x=true;
        while(x==true){
            int ch=menu();
            switch (ch){
                case 1:
                    sum(); break;
                case 2:
                    sub(); break;        
                case 3:
                    multiply(); break;
                case 4:
                    divide(); break;
                default: 
                System.out.println("Invalid option");
            }
            char ans;
            System.out.print("\nDo you want to continue[y/n]: ");
            ans=sc.next().charAt(0);
            if (ans=='y')
                x=true;
            else
                x=false;
        }
    }    
}