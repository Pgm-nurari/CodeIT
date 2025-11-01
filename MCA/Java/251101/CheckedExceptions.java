import java.io.FileWriter;
import java.io.BufferedWriter;
import java.util.Scanner;
import java.io.IOException;

public class CheckedExceptions {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a sentence: ");
        String msg = scanner.nextLine();

        FileWriter fw = new FileWriter("Myfile.txt");
        BufferedWriter writer = new BufferedWriter(fw);
        
        writer.write(msg);
        writer.close();
        scanner.close();
    }
}
