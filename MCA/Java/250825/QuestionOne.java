class Bank{
    int accno;
    String accName;
    String accType;
    Float balAmt;

    public Bank(int acc_id, String name, String type, Float balance){
        this.accno = acc_id;
        this.accName = name;
        this.accType = type;
        this.balAmt = balance;
    };

    void display(){
        System.out.println("Displaying the account details of " + accName);
        String output = String.format("Account Number: %d\nAccount Name: %s\nAccount Type: %s\nBalance Amount: %f",accno,accName,accType,balAmt);
        System.out.println(output);
    };
}

public class QuestionOne {
    public static void main(String[] args) {
        Bank b = new Bank(100, "Sabhyam", "Personal", 100.23f);
        b.display();
    }
}
