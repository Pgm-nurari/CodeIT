import java.util.*;
class employees{
	int empno;
	String empname;
	String desg;
	String dept;
	int salary;

	//Construct
	employees(){
		System.out.println("This is a construct...");
		empno=0;
		empname="Employee name";
		desg="Designation";
		dept="Department";
		salary=0;
	}

	void store(int no,String name,String post,String agency,int sal){
		empno=no;
		empname=name;
		desg=post;
		dept=agency;
		salary=sal;
	}

	void show(){
		System.out.println("Employee number: \t"+empno);
		System.out.println("Employee name: \t"+empname);
		System.out.println("Designation: \t"+desg);
		System.out.println("Department: \t"+dept);
		System.out.println("Employee salary: \t"+salary);
	}
}

public class con_example{
	static Scanner sc=new Scanner(System.in);
	public static void main(String args[]){
		

		employees emp1=new employees();
		emp1.store(123,"Rajesh","Manager","Sales",2000000);
		emp1.show();
		employees emp2=new employees();
		emp2.store(124,"Mahesh","President","Sales",20000000);
		emp2.show();
	}
}