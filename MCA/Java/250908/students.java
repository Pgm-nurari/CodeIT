import java.util.Scanner;
class student{

    String stud_name;
    int stud_no;
    String stud_course;

    student(){
        this.stud_name="sabhyam mishra";
        this.stud_no=151;
        this.stud_course="mca ai & ds";
    }
    student(String name,int no,String course){
        this.stud_name=name;
        this.stud_no=no;
        this.stud_course=course;
    }
    void display(){
        System.err.println("name :"+stud_name);
        System.err.println("name :"+stud_no);
        System.err.println("name :"+stud_course);

    }
    void update(String course){
        this.stud_course=course;
        System.out.println("course updated....");
    }
}

class students{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        
        student s1= new student();
        s1.display();

        student s2=new student("sreeram",100,"intmca");
        s2.display();

        student s3=new student();
        s3.display();
        System.out.println("enter the details ....");
        System.out.println("name:");
        s3.stud_name=sc.next();
        System.out.println("roll number:");
        s3.stud_no=sc.nextInt();
        System.out.println("course:");
        s3.stud_course=sc.next();

    }
}
