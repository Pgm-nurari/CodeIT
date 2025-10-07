import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

def wrapList(string, max_width):
    return textwrap.wrap(string,max_width)

def main():
    string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    max_width = 4
    # string, max_width = input(), int(input())

    # Returns a wrapped text as a single string...
    result = wrap(string, max_width)
    print(result)

    # Returns a wrapped text as a list of strings...
    result = wrapList(string, max_width)
    print(result)

if __name__ == '__main__':
    main()