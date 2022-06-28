from numba import cuda
import numpy as np
from numba import uint64, float64
from tkinter import *
import math
from timeit import default_timer as timer
import colour


@cuda.jit(device=True)
def calcPoints(real, imag, max_iter):
    z = 0j
    c = complex(real, imag)
    for p in range(max_iter):
        z = z * z + c
        if abs(z) >= 2:
            return p

    return max_iter


@cuda.jit
def mandelbrot_kernel(_mbm: np.ndarray, _iters: np.ndarray, _max_iter, _x_start, _x_end, _y_start, _y_end):
    # collecting metadata for current thread position
    n = cuda.blockIdx.x
    m = cuda.threadIdx.x
    # steps for x- and y-axis
    _stepX = abs(_x_end - _x_start) / cuda.gridDim.x
    _stepY = abs(_y_end - _y_start) / cuda.blockDim.x
    # x start and end values for current thread
    _x1 = n * _stepX + _x_start
    _x2 = (n + 1) * _stepX + _x_start
    # y start and end value for current thread
    _y1 = - m * _stepY + _y_start
    _y2 = - (m + 1) * _stepY + _y_start

    stepIter = _mbm.size / (cuda.blockDim.x * cuda.gridDim.x)

    stepAx = _stepX / math.sqrt(stepIter)
    stepAy = _stepY / math.sqrt(stepIter)

    _index_mbm = int(m * stepIter * cuda.blockDim.x + n * stepIter)

    for g in range(int(math.sqrt(stepIter))):
        real_ = _x1 + stepAx * g
        for h in range(int(math.sqrt(stepIter))):
            imag_ = _y1 - stepAy * h
            _mbm[_index_mbm] = complex(real_, imag_)
            _iters[_index_mbm] = calcPoints(real_, imag_, _max_iter)
            _index_mbm += 1


def readValuesIn():
    global x1, y1, x2, y2, iters, root
    x1 = float64(float(eX1.get()))
    y1 = float64(float(eY1.get()))
    x2 = float64(float(eX2.get()))
    y2 = float64(float(eY2.get()))
    iters = uint64(int(eIters.get()))

    blockdim = 128
    griddim = 128

    d_mbm = cuda.to_device(mandelbrotMean)
    d_iter = cuda.to_device(iterations)
    n = timer()
    mandelbrot_kernel[griddim, blockdim](d_mbm, d_iter, iters, x1, x2, y1, y2)
    print(timer() - n)
    d_iter.to_host()
    d_mbm.to_host()
    multiX = abs(cv.winfo_width() / (x2 - x1))
    multiY = abs(cv.winfo_height() / y1)
    transX = cv.winfo_width() / 2
    transY = cv.winfo_height() / 2
    cv.clipboard_clear()
    for k in range(0, len(mandelbrotMean), 10):
        x = mandelbrotMean[k].real * multiX + transX
        y = -mandelbrotMean[k].imag * multiX + transY
        color = calcColor(iterations[k])
        cv.create_rectangle(x, y, x, y, fill=color, outline='')
    cv.update()
    root.update()
    print('done', multiX, transX, transY)


def calcColor(iteration):
    global iters
    step = int(iters)
    color2 = (0, 0, 0)
    color1 = (75, 0, 130)
    stepRed = (color2[0] - color1[0]) / step
    stepGreen = (color2[1] - color1[1]) / step
    stepBlue = (color2[2] - color1[2]) / step
    red = int(color1[0] + stepRed * iteration)
    green = int(color1[1] + stepGreen * iteration)
    blue = int(color1[2] + stepBlue * iteration)
    c = colour.Color(rgb=(red/255, green/255, blue/255))
    return c.get_hex_l()


x1 = 0.0
y1 = 0.0
x2 = 0.0
y2 = 0.0
stepX = 0.0
stepY = 0.0
iters = 0

mandelbrotMean = np.ones(4194304, dtype=np.complex)
iterations = np.ones(4194304, dtype=np.int)

root = Tk(screenName="Mandelbrot")

lX1 = Label(root, text="X-start-value:")
lX1.grid(column=0, row=0)
lY1 = Label(root, text="Y-start-value:")
lY1.grid(column=0, row=1)
lX2 = Label(root, text="X-end-value:")
lX2.grid(column=0, row=2)
lY2 = Label(root, text="Y-end-value:")
lY2.grid(column=0, row=3)
lIters = Label(root, text="Iterations per Point:")
lIters.grid(column=0, row=4)

eX1 = Entry(root)
eX1.grid(column=1, row=0)
eY1 = Entry(root)
eY1.grid(column=1, row=1)
eX2 = Entry(root)
eX2.grid(column=1, row=2)
eY2 = Entry(root)
eY2.grid(column=1, row=3)
eIters = Entry(root)
eIters.grid(column=1, row=4)

verify = Button(root, text="Verify", command=readValuesIn)
verify.grid(column=0, row=5, columnspan=2, ipadx=80)

cv = Canvas(root, width=500, height=500, background='lightgrey')
cv.grid(column=2, row=0, rowspan=35)

root.mainloop()

with open("C:\\Users\\Dominik Lovetinsky\\Desktop\\mandel_4.txt", "w") as exportTo:
    for i in range(len(mandelbrotMean)):
        exportTo.write(str(mandelbrotMean[i].real) + ',' + str(mandelbrotMean[i].imag) + ',' + str(iterations[i]) +
                       ",\n")
    exportTo.write("EOF\n")
