import java.io.*;

// The class to be serialized must implement Serializable
class Students implements Serializable {
    // serialVersionUID is recommended for version control of the class
    private static final long serialVersionUID = 1L;

    int studno;
    String studname;
    String programme;
    int year;

    public Students(int studno, String studname, String programme, int year) {
        this.studno = studno;
        this.studname = studname;
        this.programme = programme;
        this.year = year;
    }

    @Override
    public String toString() {
        return "Student No: " + studno + 
               "\nName: " + studname + 
               "\nProgramme: " + programme + 
               "\nYear: " + year;
    }
}

public class StudentSerialization {
    public static void main(String[] args) {
        String filename = "Students.txt";
        Students student = new Students(101, "Alice Smith", "Computer Science", 2);

        // Serialization (Writing to file)
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(filename))) {
            out.writeObject(student);
            System.out.println("Object has been serialized to " + filename);
        } catch (IOException e) {
            System.out.println("IOException during serialization: " + e.getMessage());
        }

        System.out.println("--------------------------------");

        // Deserialization (Reading from file)
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream(filename))) {
            Students deserializedStudent = (Students) in.readObject();
            System.out.println("Object has been deserialized:");
            System.out.println(deserializedStudent);
        } catch (IOException | ClassNotFoundException e) {
            System.out.println("Error during deserialization: " + e.getMessage());
        }
    }
}