/* Program to Reverse each element of a matrix... */
import java.util.*;

public class MatRev {
    int arr[][]; // Matrix elements
    int m,n;
    public MatRev(int mm,int nn){
        arr=new int[mm][nn];
        m=mm;
        n=nn;
    }
    void fillarray(){
        Scanner s=new Scanner(System.in);
        for(int i=0;i<m;i++){
            for (int j=0;j<n;j++){
                System.out.println("Enter "+i+","+j+"th element: " );
                arr[i][j]=s.nextInt();
            }
            System.out.println();
        }
        s.close();
    }
    void show(){
        for(int i=0;i<m;i++){
            for (int j=0;j<n;j++){
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
    }
    /*Function to reverse the array and store it in another array...*/
    int reverse(int n){
        int tmp=n,d,rev=0;
        while(tmp>0){
            d=tmp%10;
            tmp=tmp/10;
            rev=rev*10+d;
        }
        return rev;
    }
    void revMat(MatRev P){
        // copying p.arr into current object's array by reversing its elenents...
        arr=new int[P.arr.length][];
        for (int i=0;i<arr.length;i++){
            arr[i]=new int[P.arr[i].length];
            for (int j=0;j<arr[i].length;j++){
                arr[i][j]=reverse(P.arr[i][j]);
            }
        }
    }
    public static void main(String args[]){
        MatRev mat1=new MatRev(3,3);
        MatRev mat2=new MatRev(3,3);
        mat1.fillarray();
        System.out.println("Matrix 1 Elements: ");
        mat1.show();
        mat2.revMat(mat1);
        System.out.println("Matrix 2 Elements are: ");
        mat2.show();
    }
}