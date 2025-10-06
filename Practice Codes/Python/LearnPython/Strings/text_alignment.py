from typing import Literal

def setAlignment(word : str, align :  Literal['left', 'center', 'right'] = 'left'): 
    match (align):
        case 'left': print(word.ljust(len(word)+10,'_'))
        case 'center': print(word.center(len(word)+10,'_'))
        case 'right': print(word.rjust(len(word)+10,'_'))
        case _: print("Invalid alignment option")

def fStringAlign(word : str, align :  Literal['left', 'center', 'right'] = 'left'): 
    match (align):
        case 'left': print(f"{word:+<20}")
        case 'center': print(f"{word:+^20}")
        case 'right': print(f"{word:+>20}")
        case _: print("Invalid alignment option")
         
def stringFormat(word : str, align :  Literal['left', 'center', 'right'] = 'left'): 
    match (align):
        case 'left': print("{:-<20}".format(word))
        case 'center': print("{:-^20}".format(word))
        case 'right': print("{:->20}".format(word))
        case _: print("Invalid alignment option")         


def main():
    word = "Hello World"
    
    print(f"--------------\nText Alignment\n--------------")
    print("1. Using string functions\t2. Using F-String\t3. Using String Format\n\n")
    while(1):
        string = "\n1. Left Alignment\n2. Center Alignment\n3.Right Alignment\nChoose your options: "
        ch = int(input(string))
        print()
        match(ch):
            case 1: 
                    setAlignment(word, 'left')
                    fStringAlign(word, 'left')
                    stringFormat(word,'left')
            case 2: 
                    setAlignment(word, 'center')
                    fStringAlign(word, 'center')
                    stringFormat(word,'center')
            case 3: 
                    setAlignment(word, 'right')
                    fStringAlign(word, 'right')
                    stringFormat(word,'right')
            case _: exit(0)

if __name__ == '__main__':
    main()