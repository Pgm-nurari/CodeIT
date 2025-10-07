def countValidStones(j : str, s : str):
    """To count the stones that are also jewels...

    Args:
        j (string): String containing jewels
        s (string): String containing stones
    """
    count = 0
    for i in set(j):
        count+= (s.count(i))
    return count

def main():
    jewels = 'abcjA'
    stones = 'accACb'
    print(f"Jewels: {jewels}\nStones: {stones}")
    print(f"The number of stones that are jewels with us is: {countValidStones(jewels, stones)}")

if __name__=='__main__':
    main()