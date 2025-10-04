import time

def listComp():
    test_list = [i for i in range(1_000_000_000)]
    total = sum(i for i in test_list)
    return total


def generatorComp():
    total = sum(i for i in range(1_000_000_000))
    return total

def main():
    # Running both functions one-by-one...
    start_time = time.process_time()
    result = generatorComp()
    end_time = time.process_time()
    elapsed_time = end_time - start_time

    print(f"Sum is: {result}\nTotal time taken for the process is: {elapsed_time}")


if __name__=='__main__':
    main()