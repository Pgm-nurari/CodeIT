import java.awt.*;
import java.awt.event.*;

class eventhandling3 extends Frame{

    TextField tf;
    eventhandling3(){
        // create components
        tf = new TextField();
        tf.setBounds(60,50,170,20);
        Button b = new Button("click me");
        b.setBounds(100,120,80,30);
        // register listener
        b.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent ae){
                tf.setText("Welcome");
            }
        });
        // add components and set size, layout and visibility
        add(b);add(tf);
        setSize(300,300);
        setLayout(null);
        setVisible(true);
    }
    public static void main(String args[]){
        new eventhandling3();
    }
}