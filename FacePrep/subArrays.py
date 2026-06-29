def brute(num):
    start = end = 0
    for i in range(len(num)):
        for j in range(i, len(num)):
            start = i
            end = j
            print(num[start:end + 1])
            
def maxSum(num):
    start = end = 0
    max_sum = float('-inf')
    for i in range(len(num)):
        for j in range(i, len(num)):
            start = i
            end = j
            current_sum = sum(num[start:end + 1])
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum

def optimizedMaxSum(num):
    max_sum = float('-inf')
    for i in range(len(num)):
        sum = 0
        for j in range(i, len(num)):
            sum = sum +num[j]
            if sum > max_sum:
                max_sum = sum
    return max_sum

def optimizedMaxSumTwo(num):
    max_sum = float('-inf')
    sum = 0
    for i in range(len(num)):
        sum = sum +num[i]
        if sum > max_sum:
            max_sum = sum
        if sum < 0:
            sum = 0
    return max_sum
            
def sumOfPairs(num,target):
    pairs = []
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i] + num[j] == target:
                pairs.append((num[i], num[j]))
    return pairs

def sumOfPairsOptimized(num,target):
    pairs = []
    p1=0
    p2=len(num)-1
    num.sort()
    while p1 < p2:
        if num[p1] + num[p2] == target:
            pairs.append((num[p1], num[p2]))
            p1 += 1
            p2 -= 1
        elif num[p1] + num[p2] < target:
            p1 += 1
        else:
            p2 -= 1
    return pairs

if __name__ == "__main__":
    num = [1, 2, 3, -2, 4]
    brute(num)            
    print(maxSum(num))
    print(optimizedMaxSum(num))
    print(optimizedMaxSumTwo(num))
    print(sumOfPairsOptimized([2,6,10,5,23,15,8,19,20], 18))