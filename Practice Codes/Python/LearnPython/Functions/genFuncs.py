def myGen():
    print('this is the generator function in use:')
    yield 'a'
    yield [1,2,3]
    yield 0

def main():
    print("Testing a generator function and its uses....")
    g1 = myGen()
    print(f'The generator function object: {g1}')
    print(g1.__next__())
    print(next(g1))
    print(g1.__next__())
    # print(g1.__next__())

if __name__ == '__main__':
    main()