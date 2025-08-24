import os
import class1 as c1
import Students as Std
import class2 as c2
import class3 as c3

def Std_func():
    obj1 = Std.Students()
    print("\n")
    print(f"Institution name: {Std.Students.Inst_name}")
    obj1.output()

def class3():
    obj1 = c3.function_class(10,20)
    print(obj1.sum())
    obj2 = c3.function_class(30,40)
    print(c3.function_class.concat())
    obj3 = c3.function_class(50,60)
    print("No. of times instances made: ",c3.function_class.object_count())

def main():
    try:
        pass
    except:
        raise Exception
    finally:
        print("Exiting terminal")
        os.system('exit')


if __name__ == '__main__':
    main()