#Quinn Z Shen

import sys

def solve(tests):
    draw = True

    for test in tests:
        if not("O" in test or "." in test):
            return "X won"
        if not("X" in test or "." in test):
            return "O won"
        if draw and "." in test:
            draw = False

    if draw:
        return "Draw"
    return "Game has not completed"
    

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
            grid = list()
            for _ in range(4):
                a = list()
                line = input.readline()
                for i in line:
                    if i != "\n":
                        a.append(i)
                grid.append(a)
            input.readline()
            
            tests = list()
            tests.append(grid[0]) #row1 
            tests.append(grid[1]) #row2 
            tests.append(grid[2]) #row3 
            tests.append(grid[3]) #row4 
            tests.append([x[0] for x in grid]) #col1 
            tests.append([x[1] for x in grid]) #col2 
            tests.append([x[2] for x in grid]) #col3 
            tests.append([x[3] for x in grid]) #col4 
            tests.append([grid[x][x] for x in range(len(grid))]) #diag1
            tests.append([grid[x][-x-1] for x in range(len(grid))]) #diag2

            output.write("Case #{0}: {1}".format(case, solve(tests)) + "\n")
            
    except Exception as e:
        print e.args[0]

    print "DONE."

if __name__ == "__main__":
    main()