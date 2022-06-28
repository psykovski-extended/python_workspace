import numpy as np
from numba import uint64, float64, cuda
from timeit import default_timer as timer
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


@cuda.jit(device=True)
def mandel(x, y, max_iters):
    c = complex(x, y)
    z = 0.0j
    for i in range(max_iters):
        z = z * z + c
        if (z.real * z.real + z.imag * z.imag) >= 4:
            return i

    return max_iters


@cuda.jit
def mandel_kernel(min_x, max_x, min_y, max_y, image, iters):
    height = image.shape[0]
    width = image.shape[1]

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height

    startX, startY = cuda.grid(2)
    gridX = cuda.gridDim.x * cuda.blockDim.x
    gridY = cuda.gridDim.y * cuda.blockDim.y

    for x in range(startX, width, gridX):
        real = min_x + x * pixel_size_x
        for y in range(startY, height, gridY):
            imag = min_y + y * pixel_size_y
            image[y, x] = mandel(real, imag, iters)


def showIt():
    global cm
    sp.cla()

    nx = sp.imshow(gimage, cmap=colorMap)

    divider = make_axes_locatable(sp)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    if cm is not None:
        cm.remove()
    cm = fig.colorbar(nx, cax=cax, orientation='vertical')
    cv.draw()


def recalcImage():
    global gimage
    try:
        start = timer()

        d_image = cuda.to_device(gimage)
        mandel_kernel[griddim, blockdim](x1, x2, y1, y2, d_image, iters)
        gimage = d_image.copy_to_host()  # to_host()

        dt = timer() - start
        time.set('Created in ' + f'{dt:.7f}' + 's')
    except Exception as e:
        print(e)
        time.set('Error occurred, kernel has shut down!\n' + str(e))


def deleteAndInsert():
    eYp.delete(0, 'end')
    eYp.insert(0, str(y))

    eXp.delete(0, 'end')
    eXp.insert(0, str(x))

    eLim.delete(0, 'end')
    eLim.insert(0, str(radius))

    eX1.delete(0, 'end')
    eX1.insert(0, str(x1))

    eX2.delete(0, 'end')
    eX2.insert(0, str(x2))

    eY1.delete(0, 'end')
    eY1.insert(0, str(y1))


def readValuesIn():
    global x, y, x1, y1, x2, y2, iters, root, xd, yd, colorMap, radius
    x1 = float64(float(eX1.get()))
    y1 = float64(float(eY1.get()))
    x2 = float64(float(eX2.get()))
    y2 = y1 - abs(x1 - x2)

    x = x1 + (x2 - x1) / 2
    y = y1 - (y1 - y2) / 2

    radius = abs(x2 - x1) / 2
    deleteAndInsert()
    iters = uint64(eIters.get())

    getColorMap()
    recalcImage()
    showIt()


def getColorMap():
    global colorMap, eCmap
    try:
        colorMap = eCmap.get()
        showIt()
    except Exception as ex:
        colorMap = cmaps[index]
        showIt()
    if colorMap == '':
        colorMap = 'nipy_spectral_r'


def zoom(e):
    global x, y, x1, x2, y1, y2, iters, radius
    radius = abs(float64(eLim.get()))
    if e != '':
        x = float64(eXp.get())
        y = float64(eYp.get())

    if e == 'In':
        InOut = 0.8
    elif e == 'Out':
        InOut = 1.2
    else:
        InOut = 1

    radius *= InOut
    x1 = x - radius
    x2 = x + radius
    y1 = y + radius
    deleteAndInsert()

    y2 = y - radius
    iters = uint64(eIters.get())
    recalcImage()
    showIt()


def nextCmap():
    global cmaps, index, colorMap
    index += 1
    index %= len(cmaps)
    eCmap.delete(0, 'end')
    eCmap.insert(0, str(cmaps[index]))
    colorMap = cmaps[index]
    showIt()


def prevCmap():
    global cmaps, index, colorMap
    index -= 1
    if index < 1 - len(cmaps):
        index = 0
    eCmap.delete(0, 'end')
    eCmap.insert(0, str(cmaps[index]))
    colorMap = cmaps[index]
    showIt()


def move(e):
    global x, y, radius
    into = radius / 10
    if e == 'up':
        y += into
    elif e == 'down':
        y -= into
    elif e == 'right':
        x += into
    elif e == 'left':
        x -= into
    zoom('')


x1 = -2
y1 = 1.5
x2 = 1
y2 = -1.5
x = x1 + (x2 - x1) / 2
y = y1 - (y1 - y2) / 2
iters = 30
colorMap = 'nipy_spectral_r'
xd = 1580
yd = 1580
radius = 0
cm = None

gimage = np.zeros((xd, yd), dtype=np.uint16)
blockdim = (64, 8)
griddim = (256, 256)  # (64, 32)

root = Tk()
# root.iconbitmap('C:\\Users\\Dominik Lovetinsky\\Desktop\\Python\\mbico.ico')
root.title('Mandelbrot Calculator')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

entry = Frame(root, width=350, bg='#001f3f')
entry.grid(row=0, column=0, rowspan=2, sticky="nsew")
matlabFrame = Frame(root, bg='grey')
matlabFrame.grid(row=0, column=1)

cmaps = plt.colormaps()
index = cmaps.index('nipy_spectral_r')
time = StringVar(entry)

font = ('JetBrains Mono', 14)

lRange = Label(entry, text="Range-Zoom", font=('JetBrains Mono', 18), bg='#001f3f', fg='#20b2aa')
lRange.grid(column=0, row=0, columnspan=2, stick='we')
lPoint = Label(entry, text="Point-Zoom", font=('JetBrains Mono', 18), bg='#001f3f', fg='#20b2aa')
lPoint.grid(column=0, row=7, columnspan=2, stick='we')
lX1 = Label(entry, text="X1:", font=font, bg='#001f3f', fg='white')
lX1.grid(column=0, row=1)
lY1 = Label(entry, text="Y1:", font=font, bg='#001f3f', fg='white')
lY1.grid(column=0, row=2)
lX2 = Label(entry, text="X2:", font=font, bg='#001f3f', fg='white')
lX2.grid(column=0, row=3)
lIters = Label(entry, text="Iter.:", font=font, bg='#001f3f', fg='white')
lIters.grid(column=0, row=4)
lCmap = Label(entry, text="Cmap:", font=font, bg='#001f3f', fg='white')
lCmap.grid(column=0, row=13)
lXp = Label(entry, text='X:', font=font, bg='#001f3f', fg='white')
lXp.grid(column=0, row=8)
lYp = Label(entry, text='Y:', font=font, bg='#001f3f', fg='white')
lYp.grid(column=0, row=9)
lLim = Label(entry, text='Radius:', font=font, bg='#001f3f', fg='white')
lLim.grid(column=0, row=10)
lColorMap = Label(entry, text='Colormap', font=('JetBrains Mono', 18), bg='#001f3f', fg='#20b2aa')
lColorMap.grid(column=0, row=12, columnspan=2, stick='we')
lTime = Label(entry, textvariable=time, font=font, bg='#001f3f', fg='#6f112b')
lTime.grid(column=0, row=15, columnspan=5)

eX1 = Entry(entry, font=font)
eX1.grid(row=1, column=1, columnspan=2)
eY1 = Entry(entry, font=font)
eY1.grid(row=2, column=1, columnspan=2)
eX2 = Entry(entry, font=font)
eX2.grid(row=3, column=1, columnspan=2)
eIters = Entry(entry, font=font)
eIters.grid(row=4, column=1, columnspan=2)
eCmap = Entry(entry, font=font)
eCmap.grid(row=13, column=1, columnspan=2)
eXp = Entry(entry, font=font)
eXp.grid(column=1, row=8, columnspan=2)
eYp = Entry(entry, font=font)
eYp.grid(column=1, row=9, columnspan=2)
eLim = Entry(entry, font=font)
eLim.grid(column=1, row=10, columnspan=2)

eX1.insert(0, x1)
eX2.insert(0, x2)
eY1.insert(0, y1)
eIters.insert(0, iters)
eCmap.insert(0, colorMap)
eXp.insert(0, x)
eYp.insert(0, y)
eLim.insert(0, abs(x2 - x1) / 2)

verify = Button(entry, text="Calculate", command=readValuesIn, font=font, relief=GROOVE, bd=2, bg='#001f2d', fg='grey')
verify.grid(row=6, column=0, columnspan=3, sticky='e')
zoomIn = Button(entry, text=' + ', command=lambda: zoom('In'), font=font, relief=GROOVE, bd=2, bg='#001f2d', fg='grey')
zoomIn.grid(row=11, column=1, sticky='e')
zoomOut = Button(entry, text=' - ', command=lambda: zoom('Out'), font=font, relief=GROOVE, bd=2, bg='#001f2d',
                 fg='grey')
zoomOut.grid(row=11, column=2, sticky='w')
nextColor = Button(entry, text=chr(0x2964), command=nextCmap, font=('JetBrains Mono', 10), relief=GROOVE, bd=2,
                   bg='#001f2d', fg='grey', width=4)
nextColor.grid(row=13, column=4)
prevColor = Button(entry, text=chr(0x2962), command=prevCmap, font=('JetBrains Mono', 10), relief=GROOVE, bd=2,
                   bg='#001f2d', fg='grey', width=4)
prevColor.grid(row=13, column=3)
xLeft = Button(entry, text=chr(0x2b9c), command=lambda: move('left'), font=('JetBrains Mono', 10), relief=GROOVE, bd=2,
               bg='#001f2d', fg='grey', width=4)
xLeft.grid(row=8, column=3)
xRight = Button(entry, text=chr(0x2b9e), command=lambda: move('right'), font=('JetBrains Mono', 10), relief=GROOVE,
                bd=2, bg='#001f2d', fg='grey', width=4)
xRight.grid(row=8, column=4)
yUp = Button(entry, text=chr(0x2b9d), command=lambda: move('up'), font=('JetBrains Mono', 10), relief=GROOVE, bd=2,
             bg='#001f2d', fg='grey', width=4)
yUp.grid(row=9, column=4)
yDown = Button(entry, text=chr(0x2b9f), command=lambda: move('down'), font=('JetBrains Mono', 10), relief=GROOVE, bd=2,
               bg='#001f2d', fg='grey', width=4)
yDown.grid(row=9, column=3)
getCMap = Button(entry, text=chr(0x22d9), command=getColorMap, font=('JetBrains Mono', 10), relief=GROOVE, bd=2,
                 bg='#001f2d', fg='grey', width=4)
getCMap.grid(row=14, column=2, stick='e')

eCmap.bind('<Return>', getColorMap)

fig = Figure(figsize=(8, 8), facecolor='#254b70')
sp = fig.add_subplot(111, fc='white')
cv = FigureCanvasTkAgg(fig, matlabFrame)
cv.get_tk_widget().pack()
navigation = NavigationToolbar2Tk(cv, matlabFrame)

recalcImage()
showIt()

root.mainloop()
