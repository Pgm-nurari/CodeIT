
class emp{
    int empno;
    String empname;

    emp()
    {
        empno=104;
        empname="rahul";

    }

    emp(int no,String name )
        {
            empno=no;
            empname= name;
            System.err.println("constructor executed");
        }
    
    void display_message(){
        System.out.println("welcome to "+empno+","+empname);
    }

    
}

class constructor{
    public static void main(String[] args)
    {
        emp e1=new emp(101,"sam");
        e1.display_message();

        emp e2=new emp(103,"tom");
        e2.display_message();

        emp e3=new emp();
        e3.display_message();
    }
}