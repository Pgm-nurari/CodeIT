import java.awt.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class CanvasExample {
    
    public CanvasExample(){
        Frame f1=new Frame("Canvas Example");
        f1.add(new MyCanvas());

        f1.setLayout(null);
        f1.setSize(600,600);
        f1.setVisible(true);

        f1.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent we){
                System.exit(0);
            }
        });
    }
    public static void main(String[] args) {
        new CanvasExample();
    }
}

class MyCanvas extends Canvas{
    public MyCanvas(){
        setBackground(Color.CYAN);
        setLocation(150,150);
        setSize(300,300);
    }
    public void paint(Graphics g){
        g.setColor(Color.red);
        g.fillOval(75,75,150,150);
    }
}