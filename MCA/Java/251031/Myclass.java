/*Cannot change the value after FINAL , It declare the var as constant 
 * Final in method : cannot be overridden in its derived class 
 * In Class : Final will not allow to inherited by any other class
 */
final class Testing
{
    final double pi = 3.141;
    final int a = 5;

    public Testing()
    {
        a = 10;
    }
    final void hello()
    {
        System.err.println("HEllo");
    }
    
}
class Myclass extends Testing //Final blocks the inheritance
{
    void hellso()// Method overriding 
    {
        System.err.println("Hello from MyClass");
    }
}