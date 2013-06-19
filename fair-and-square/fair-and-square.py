#Quinn Z Shen

import sys
import math

memo = dict()
memo_ana = dict()

def isFairAndSquare(num):
    square = math.sqrt(num)
    if square == int(square) and isFair(num):
        return 1
    return 0

def isFair(num):
    if num in memo_ana:
        return memo_ana[num]
    else:
        i = int(math.ceil(num/2))
        if str(num)[i:] == str(num)[:-i]:
            memo_ana[num] = True
        else:
            memo_ana[num] = False
        return memo_ana[num]

def solve(lower_limit, upper_limit):
    num = lower_limit
    count = 0
    while num < upper_limit:
        if num in memo:
            count += memo[num]
        else:
            memo[num] = isFairAndSquare(num)
        num += 1 
    return count

def main():
    try:
        args = sys.argv[1:]
        if len(args) != 1:
            raise Exception("Error: Expected only 1 argument.")
        if args[0][-2:] != "in":
            raise Exception("Error: Expected .in file type.")
        input = open(args[0], 'r')
        output = open(args[0][:-2] + "out", 'w')

        total_cases = int(input.readline())

        for case in range(1, total_cases + 1):
            line = (input.readline()).split()
            a, b = int(line[0]), int(line[1])

            output.write("Case #{0}: {1}".format(case, solve(a, b)) + "\n")
            
    except Exception as e:
        print e.args[0]

    print "DONE."

if __name__ == "__main__":
    main()