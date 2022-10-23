def solution(n):
    n = int(n)

    res = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        elif (n == 3) or (n % 4 == 1):
            n -= 1
        elif n % 4 == 3:
            n += 1
        res += 1

    return res

if __name__ == "__main__":
    print(solution('4')) #2

    print(solution('15')) #5

    print(solution("15"))
    print(solution("13"))

    print(solution("4") == 2)
    print(solution("15") == 5)
    print(solution("13") == 5)
    print(solution("9") == 4)
    print(solution("2") == 1)
    print(solution("1") == 0)
