class Students{
    int studno;
    String studname;
}

class Employee{
    int emno;
    String empname;
    String des;
}

public class Main{
    public static void main(String [] args){
        Students s1 = new Students();
        s1.studno = 30;
        s1.studname = "Sabhyam";

        System.out.println(s1);

        Employee e1 = new Employee();
        e1.emno = 10;
        e1.empname = "JK";
        e1.des = "Cloud Engineer";

        Employee e2 = new Employee();
        e2.emno = 10;
        e2.empname = "JK";
        e2.des = "Cloud Engineer";

        Employee e3 = new Employee();
        e3.emno = 10;
        e3.empname = "JK";
        e3.des = "Cloud Engineer";
        
        System.out.println("e1: emno=" + e1.emno + ", empname=" + e1.empname + ", des=" + e1.des);
        System.out.println("e2: emno=" + e2.emno + ", empname=" + e2.empname + ", des=" + e2.des);
        System.out.println("e3: emno=" + e3.emno + ", empname=" + e3.empname + ", des=" + e3.des);
    }
}