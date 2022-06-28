from numpy import *
import sys


if __name__ == '__main__':
    func = sys.argv[1]
    print(func)
    func.replace(" ", "")
    x1 = float(sys.argv[2])
    x2 = float(sys.argv[3])

    exec(func[2] + '=linspace(x1__inv, x2_inv, 10000)')
    func = func[5:]
    x = linspace(x1, x2, 10000)
    y = eval(func)
    for i in range(y.size):
        print(str(y[i]) + ',' + str(x[i]) + '\n')
    print('\n')
