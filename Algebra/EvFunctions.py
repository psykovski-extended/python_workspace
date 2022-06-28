import math
import matplotlib.pyplot as plt
from sympy import *


class EvFunction:

    def __init__(self, funcStr="", varFunc="x"):
        """
        'originalStr' is the string you are parsing to here;
        'functionStr' is the organized string, which can be executed by typing eval(functionStr);
        'definitionM' is the definition mean, in which this function is allowed to evaluate;
        """
        self.originalStr = funcStr
        self.functionStr = ""
        self.funcVariable = varFunc

        self.x = []
        self.fx = []
        
        self.replacements = []
        self.organizeFunctionStr()
        self.rootVariables()

        exec(varFunc + ' = symbols("' + varFunc + '")')
        self.ca_Object = eval(self.originalStr)
        # self.definitionM = self.definitionMean()

    def __del__(self):
        pass

    def __str__(self):
        return self.functionStr

    def definitionMean(self):
        pass

    def displayFunction(self, color='b', typ='-', grid=False, _xLabel="", _yLabel=""):
        plt.plot(self.x, self.fx, typ + color)
        if grid:
            plt.grid()
        plt.xlabel(_xLabel)
        plt.ylabel(_yLabel)
        plt.show()

    def exportGraph(self, filename, _format='png', resolution=500):
        with open(filename) as f:
            plt.plot(self.x, self.fx)
            plt.savefig(fname=f, format=_format, dpi=resolution)

    def toDict(self):
        functionPoints = {}
        for i in range(len(self.fx)):
            functionPoints.update({self.x[i], self.fx[i]})
        return functionPoints

    def integrate__(self):
        exec(self.funcVariable + ' = symbols("' + self.funcVariable + '")')
        return EvFunction(str(integrate(self.ca_Object)), self.funcVariable)

    def diff__(self):
        exec(self.funcVariable + ' = symbols("' + self.funcVariable + '")')
        print(locals())
        return EvFunction(str(diff(self.ca_Object)), self.funcVariable)

    def toLaTeX(self):
        return latex(self.ca_Object)

    def evaluate(self, x_arr):
        for i in x_arr:
            self.x.append(i)
            s = self.replaceChar(i)
            self.fx.append(eval(s))
        return self.x, self.fx

    def organizeFunctionStr(self):
        funcStr = self.originalStr
        if "^" in funcStr:
            funcStr = funcStr.replace("^", "**")
        if "asin" in funcStr:
            funcStr = funcStr.replace("asin", "math.asin")
        if "acos" in funcStr:
            funcStr = funcStr.replace("acos", "math.acos")
        if "atan" in funcStr:
            funcStr = funcStr.replace("atan", "math.atan")
        if "sin" in funcStr:
            funcStr = funcStr.replace("sin", "math.sin")
        if "cos" in funcStr:
            funcStr = funcStr.replace("cos", "math.cos")
        if "tan" in funcStr:
            funcStr = funcStr.replace("tan", "math.tan")
        self.functionStr = funcStr

    def readInFunc(self):
        # reading in function
        funcStr = input("Please enter a function: ")
        funcChr = input("Please determine your variable: ")
        self.originalStr = funcStr
        self.organizeFunctionStr()
        self.funcVariable = funcChr

    def replaceChar(self, digit: float):
        funcStr = list(self.functionStr)
        off = 0
        expr = '(' + str(digit) + ')'
        for i in self.replacements:
            for j in range(len(expr)):
                if j == 0:
                    funcStr[i + j + off] = list(expr)[j]
                else:
                    funcStr.insert(i + j + off, list(expr)[j])
            off += (len(list(expr))-1)
        return ''.join(funcStr)

    def rootVariables(self):
        i = 0
        while i < len(self.functionStr):
            step1 = False
            step2 = False

            if i > 0:
                n = ord(self.functionStr[i - 1])
            else:
                n = 0x2B

            if n == 0x2A or n == 0x2B or n == 0x2D or n == 0x2F or n == 0x28:
                step1 = True

            if i < len(self.functionStr) - 1:
                n = ord(self.functionStr[i + 1])
            else:
                n = 0x2B

            if n == 0x2A or n == 0x2B or n == 0x2D or n == 0x2F or n == 0x29:
                step2 = True

            if self.functionStr[i] == self.funcVariable and step1 and step2:
                self.replacements.append(i)
            i += 1

    def simplifyStr(self):
        fs = self.originalStr
        for i in range(-9, 9):
            uni = getPotencyOf(abs(i))
            ar = str(chr(8315)) + str(uni) if i < 0 else uni
            fs = fs.replace("**" + str(i), ar)
        fs = fs.replace("*", "")
        return fs


def getPotencyOf(i: int):  # TODO fertigstellen!
    if i == -1:
        return chr(8303)
    elif i == 0:
        return chr(184)
    elif i == 1:
        return chr(177)
    elif i == 2:
        return chr(178)
    elif i <= 8:
        return chr(8303 + i)


def main():
    f1 = EvFunction("2*x**5-2*x-3")
    fx = f1.evaluate(-7, 7, 0.5)

    print(fx)
    # f2 = EvFunction("")
    # xr,fxr = f2.readInFunc()
    # sth = f2.simplifyStr()
    fsin = EvFunction("2*sin(x)")
    fsin.organizeFunctionStr()
    print(fsin.simplifyStr())
    fsin.evaluate(0, math.pi, 0.01)
    fxSin = fsin.toDict()
    print(f"{'x':>10}{'f(x)':>10}")
    xs = list(fxSin.keys())
    fxs = list(fxSin.values())
    for i in range(len(xs)):
        print("{0:10.3f}{1:10.3f}".format(xs[i], fxs[i]))

    # ft = EvFunction("")
    # xp, fxp = ft.readInFunc()
    # print(f"{'x':>20}{'f(x)':>20}")
    # for i in range(len(xp)):
    #    print("{0:20.10f}{1:20.10f}".format(xp[i],fxp[i]))
    # print(ft)
    # print(sth)

    del f1
    del fsin


if __name__ == "__main__":
    main()
