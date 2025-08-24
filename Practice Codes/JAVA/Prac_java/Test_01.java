import java.util.*;
public class Test_01{
    static Scanner sc=new Scanner(System.in);
    public static void main(String args[]){
        int arr2[]=new int[10];
        int arr1[]=new int[10];
        for (int f=0;f<10;f++){
            arr2[f]=sc.nextInt();
        }
        for (int f=0;f<10;f++){
            arr1[f]=arr2[f];
        }
        int n1=0,n2=0;
        for (int f=0;f<10;f++){
            if (f==0)
                n2=arr1[f];
            else if (arr1[f]>n2){
                n1=n2;
                n2=arr1[f];
            }
        }        
        System.out.println("Second Largets is:");
        System.out.println(n1);
        
    }
}
