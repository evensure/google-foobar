import numpy as np
import pandas as pd
from icecream import ic

def solution(m):
    #m = np.array(m)
    n = len(m)
    m = pd.DataFrame(m)

    #standard form
    idx_terminal = []
    #row_sum = [] #divisor for standard form
    for idx, row in m.iterrows():
        if row.sum() == 0:
            idx_terminal.append(idx)
            row[idx] = 1
        #row_sum.append(sum(row))
    idx_nonterminal = [i for i in range(n) if i not in idx_terminal]

    m = m.reindex(idx_terminal + idx_nonterminal, columns = idx_terminal + idx_nonterminal)
    m['row_sum'] = m.sum(axis=1)

    return m
    #return m[max(idx_terminal):n, 0:idx_terminal]




if __name__ == "__main__":
    print(solution([[0, 2, 1, 0, 0],
                    [0, 0, 0, 3, 4],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]])) # [7, 6, 8, 21]
    print(solution([[0, 1, 0, 0, 0, 1],
                    [4, 0, 0, 3, 2, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]])) # [0, 3, 2, 9, 14]
