import java.util.*;
class students{
    int rollno;
    String name;
    int m1,m2,m3;
}

class stud_class{
    static Scanner sc=new Scanner(System.in);
    public static void main(String arg[]){
        System.out.println("Enter rollno, name, m1, m2, m3.");

        System.out.println("Student 1: ");
        students s1=new students();
        s1.rollno=sc.nextInt();
        s1.name=sc.next();
        s1.m1=sc.nextInt();
        s1.m2=sc.nextInt();
        s1.m3=sc.nextInt();

        System.out.println("Student 2: ");
        students s2=new students();
        s2.rollno=sc.nextInt();
        s2.name=sc.next();
        s2.m1=sc.nextInt();
        s2.m2=sc.nextInt();
        s2.m3=sc.nextInt();        
                
        sc.close();
    }

}
