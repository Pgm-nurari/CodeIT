import java.awt.Button;
import java.awt.Frame;
import java.awt.Label;
import java.awt.List;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

class ListExample{

    Frame f1=new Frame();
    final Label l1=new Label();
    Button b= new Button("Show");
    final List list1=new List(4,false);
    final List list2=new List(4,false);

    public ListExample(){
        l1.setAlignment(Label.CENTER);
        l1.setSize(500,100);

        b.setBounds(200,150,80,30);
        b.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent ae){
                String data = "Programming language selected: " + list1.getItem(list1.getSelectedIndex());
                data  = data + ", Framework Selected: ";
                for(String frame: list2.getSelectedItems()){
                    data = data + frame + "  ";
                }
                l1.setText(data);
            }
        });

        list1.setBounds(100,100,70,70);
        list1.add("C");
        list1.add("C++");
        list1.add("Java");
        list1.add("PHP");

        list2.setBounds(100,200,70,70);
        list2.add("TurboC++");
        list2.add("Spring");
        list2.add("Hibernate");
        list2.add("CodeIgnitor");

        f1.add(list1);
        f1.add(list2);
        f1.add(l1);
        f1.add(b);

        f1.setSize(450,450);
        f1.setLayout(null);
        f1.setVisible(true);

        f1.addWindowListener(new WindowAdapter() {
           public void windowClosing(WindowEvent we){
            System.exit(0);
           } 
        });
    }

    public static void main(String args[]){
        new ListExample();
    }
}
