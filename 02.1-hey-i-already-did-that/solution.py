import numpy as np

def solution(n, b):
    '''
    n: minion ID of length k in base b
    b: base of number n (constr: 2 <= b <= 10)
    k_n: length of n (constr: 2 <= k <= 9)
    '''
    k_n = len(n)
    list_of_id = []

    while n not in list_of_id:
        list_of_id.append(n)
        y = ''.join(sorted(n))
        x = y[::-1]
        '''
        x: n descending
        y: n ascending
        '''
        y = ''.join(sorted(n))
        x = y[::-1]
        # z_int: integer represantation of z for base b
        z_int = int(x, b) - int(y, b)
        # k_z: length of z without padding
        k_z = len(np.base_repr(z_int, b))
        # z: string represantation of z_int for base b b
        z = np.base_repr(z_int, b, k_n - k_z)
        # n: z becomes new minion ID
        n = z
    return len(list_of_id[list_of_id.index(n):])


if __name__ == "__main__":
    print(solution('1211', 10)) #1

    print(solution('210022', 3)) #3
