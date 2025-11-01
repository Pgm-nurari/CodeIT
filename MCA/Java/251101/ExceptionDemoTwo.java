class ExceptionDemoTwo{
    public static void main(String[] args) {
        System.out.println("Welcome");
        
        try 
        {
            System.out.println(args[0]);
            int a = Integer.parseInt(args[0]);
            int b = Integer.parseInt(args[1]);
            System.out.println("Result: " + (a / b));
            System.out.println("End of try block");
        }
        
        catch (ArrayIndexOutOfBoundsException e) 
        {
            System.out.println("Default");
        }

        catch (NumberFormatException e)
        {
            System.out.println("Please provide integer values");
        }
        
        catch (ArithmeticException e)
        {
            System.out.println("Denominator cannot be zero");
        }
        
        catch (Exception e)
        {
            System.out.println("Some other exception occurred");
        }

        System.out.println("Good bye");
    }
}
