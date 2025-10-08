def checkIfBlack(board : list,cellname : str):
    column = ord(cellname[0]) - 97
    row = int(cellname[1]) - 1

    if (board[row][column]==1):
        return True
    else:
        return False

def main():
    board = [
        [1,0,1,0,1],
        [0,1,0,1,0],
        [1,0,1,0,1]
    ]

    result = checkIfBlack(board, 'a1')

    print(f" a1 is black? {result}")
    

if __name__=='__main__':
    main()