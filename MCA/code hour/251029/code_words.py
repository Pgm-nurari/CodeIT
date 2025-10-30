def decode():
    code = input()
    new_code = ''
    i=0
    while i<len(code):
        if code[i]=='#':
            i+=1
            continue
        if ((i+2)<=(len(code)-1) and code[i+2]=='#'):
            v = code[i:i+2]
            cl = chr(int(v)+96)
            new_code+=cl
            i+=3
        else:
            v = code[i]
            cl = chr(int(v)+96)
            new_code+=cl
            i+=1
    print(new_code)
def main():
    decode()

if __name__=='__main__':
    main()