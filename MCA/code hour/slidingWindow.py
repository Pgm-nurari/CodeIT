def main():
    arr : list = [1,2,3,4,5,6,7,8,9,11,12,13]
    window_length = 3

    for i in range(len(arr) - window_length+1):
        print(arr[i:i+(window_length)])    

    print('Without using the slicing....')

    for i in range(len(arr) - window_length+1):
        print(arr[i+0],arr[i+1],arr[i+2], sep = " ")
    

if __name__=='__main__':
    main()