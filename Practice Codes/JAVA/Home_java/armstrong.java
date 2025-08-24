import java.util.*;

class arm_num{
    int n;
    public int digits(int num){
        int count=0;
        while (num>0){
            num=num/10;
            count++;
        }
        return count;
    }
    public double sum_num(int num){
        int r;
        double s=0.0;
        int d=digits(num);
        while (num>0){
            r=num%10;
            num=num/10;
            s=s+Math.pow(r,d);
        }
        return s;
    }
    public void is_arm(int n){
        double sum=sum_num(n);
        if (n==sum){
            System.out.println(sum +" is an armstrong.");
        }
        else{
            System.out.println(sum +" is not an armstrong.");
        }
    }
}

class armstrong{
    static Scanner sc=new Scanner(System.in);
    public static void main(String arg[]){
        arm_num num1=new arm_num();
        arm_num num2=new arm_num();
        arm_num num3=new arm_num();
        num1.is_arm(371);
        num2.is_arm(54748);
        num3.is_arm(101);
    }
}