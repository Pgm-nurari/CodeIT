class ExceptionDemo{
    public static void main(String[] args) {
        System.out.println("Welcome");
        
        try 
        {
            System.out.println(args[0]);
        }
        
        catch (ArrayIndexOutOfBoundsException e) 
        {
            System.out.println("Default");
        }
        
        System.out.println("Good bye");
    }
}

/*
 * try
 * {
 *  Must be attached with either a catch or finally block...
 *  Chance of having exception - statements...
 * }
 * 
 * catch ( <type of error that occured> )
 * {
 *  Statements to be exceuted when exception occurs...
 * }
 * 
 * finally
 * {
 *  Always gets executed whether exception occurs or not...
 * }
 * 
 * throws
 * except
 */