def solution(pegs):
    num_gears = len(pegs)
    # impossible if one or less pegs
    if ((num_gears == 1) or not pegs):
        return [-1, -1]



if __name__ == "__main__":
    solution([4, 30, 50]) #12,1

    solution([4, 17, 50]) #-1,-1
