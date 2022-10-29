def solution(l):
    n = len(l)
    divisor_couples = [0] * n

    for i in range(1, n-1):
        for j in range(i):
            if l[i] % l[j] == 0:
                divisor_couples[i] += 1

    cnt = 0
    for i in range(2, n):
        for j in range(1, i):
            if l[i] % l[j] == 0:
                cnt += divisor_couples[j]

    return cnt

def solution(l):
    n = len(l)
    div_pairs = [0] * n
    cnt = 0
    for i in range(0, n):
        #j = 0
        for j in range(0, i):
            if l[i] % l[j] == 0:
                div_pairs[i] += 1
                cnt += div_pairs[j]
    return cnt





if __name__ == "__main__":
    print(solution([1, 2, 3, 4, 5, 6])) #3 [[1, 2, 4], [1, 2, 6], [1, 3, 6]]
    print(solution([1, 1, 1])) #1
    print(solution([6, 2, 3, 4, 5, 1])) #3 [[1, 2, 4], [1, 2, 6], [1, 3, 6]]
    '''
    print (answer("4") == 2)
    print (answer("15") == 5)
    print (answer("13") == 5)
    print (answer("9") == 4)
    print (answer("2") == 1)
    print (answer("1") == 0)
    '''
