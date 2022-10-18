def solution(n, b):
    '''
    param n: minion ID of length k in base b
    type n: str
    param b: base of number n (constr: 2 <= b <= 10)
    type b: int
    '''
    # param k: length of n (constr: 2 <= k <= 9)
    # type k: int
    k = len(n)


    # x: n descending, y: n ascending
    y = ''.join(sorted(n))
    x = y[::-1]
    # z: x - y with preceding zeros to keep length k
    z = str(int(x) - int(y))
    z = (k - len(x)) * '0' + z
    n = z
    print(n)
    return(z, k)

if __name__ == "__main__":
    print(solution('1211', 10)) #1

    print(solution('210022', 3)) #3
