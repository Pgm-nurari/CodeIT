from typing import Literal

def setAlignment(word : str, align :  Literal['left', 'center', 'right'] = 'left'): 
    match (align):
        case 'left': print(word.ljust(len(word)+10,'_'))
        case 'center': print(word.center(len(word)+10,'_'))
        case 'right': print(word.rjust(len(word)+10,'_'))
        case _: print("Invalid alignment option")

def main():
    word = "Hello World"
    
    print(f"--------------\nText Alignment\n--------------")
    while(1):
        string = "1. Left Alignment\n2. Center Alignment\n3.Right Alignment\nChoose your options: "
        ch = int(input(string))
        match(ch):
            case 1: setAlignment(word, 'left')
            case 2: setAlignment(word, 'center')
            case 3: setAlignment(word, 'right')
            case _: exit(0)

if __name__ == '__main__':
    main()