import threading
import time
import random
from queue import SimpleQueue
from tkinter import *


class Snake:

    def __init__(self, master, color='#556b2f', colorFood='#dc143c', width=20, height=20, startElements=3):
        if startElements < 1 or startElements > 10:
            startElements = 5
        x = width * startElements
        y = height * 2
        self.master = master
        self.x = []
        self.y = []
        self.startElements = startElements
        self.color = color
        self.colorFood = colorFood
        self.width = width
        self.height = height
        self.colorCV = '#20B2AA'
        self.cv = Canvas(self.master, bg=self.colorCV, width=20 * self.width, height=20 * self.height)
        self.master.bind('<KeyPress-Left>', lambda e: self.addMovement('Left'))
        self.master.bind('<KeyPress-Right>', lambda e: self.addMovement('Right'))
        self.master.bind('<KeyPress-Up>', lambda e: self.addMovement('Up'))
        self.master.bind('<KeyPress-Down>', lambda e: self.addMovement('Down'))
        self.master.bind('<KeyPress-a>', lambda e: self.addMovement('Left'))
        self.master.bind('<KeyPress-d>', lambda e: self.addMovement('Right'))
        self.master.bind('<KeyPress-w>', lambda e: self.addMovement('Up'))
        self.master.bind('<KeyPress-s>', lambda e: self.addMovement('Down'))
        self.snake = []
        self.queue = SimpleQueue()
        self.currentDirection = 'Right'
        self.runGame = False
        self.gameOver = False
        self.labelGameOver = 0
        self.score = 0
        self.foodX = 10 * self.width
        self.foodY = 10 * self.height
        self.food = self.cv.create_rectangle(self.foodX, self.foodY, self.foodX + self.width,
                                             self.foodY + self.height, fill=self.colorFood, outline=self.colorCV)
        for i in range(startElements):
            self.x.append(x - width * i)
            self.y.append(y)
            self.snake.append(self.cv.create_rectangle(self.x[i], self.y[i],
                                                       self.x[i] + self.width, self.y[i] + self.height,
                                                       fill=color, outline=self.colorCV))
        self.t1 = threading.Thread(target=self.moveLoop)
        self.t2 = threading.Thread(target=self.isFoodReached)
        self.t3 = threading.Thread(target=self.isTailBittenOrBorderReached)
        self.t1.start()
        self.t2.start()
        self.t3.start()

    def startGame(self):
        self.runGame = True

    def pauseGame(self):
        self.runGame = False

    def isTailBittenOrBorderReached(self):
        while self.t3.is_alive():
            if self.x[0] < 0 or self.x[0] >= self.width * 20 or self.y[0] < 0 or self.y[0] >= self.height * 20:
                self.gameOver = True
            for i in range(1, len(self.x)):
                if self.x[0] == self.x[i] and self.y[0] == self.y[i]:
                    self.gameOver = True
                    break
            if self.gameOver:
                self.labelGameOver = self.cv.create_text(self.cv.winfo_width() / 2, self.cv.winfo_height() / 2,
                                                         text='Game Over!', font=('JetBrains Mono', 35))
                break
            time.sleep(0.1)

    def isFoodReached(self):
        while self.t2.is_alive():
            if self.runGame and not self.gameOver:
                for i in range(len(self.snake)):
                    if self.x[i] == self.foodX and self.y[i] == self.foodY:
                        self.score += 20
                        self.cv.delete(self.food)
                        xt = self.x[-1] - (self.x[-2] - self.x[-1])
                        yt = self.y[-1] - (self.y[-2] - self.y[-1])
                        self.snake.append(self.cv.create_rectangle(xt, yt,
                                                                   xt + self.width, yt + self.height,
                                                                   fill=self.color, outline=self.colorCV))
                        self.x.append(xt)
                        self.y.append(yt)
                        random.seed()
                        nx = random.randint(1, 19)
                        ny = random.randint(1, 19)
                        self.foodX = nx * self.width
                        self.foodY = ny * self.height
                        for j in range(len(self.x)):
                            if self.foodX == self.x[i] and self.foodY == self.y[i]:
                                random.seed()
                                nx = random.randint(1, 19)
                                ny = random.randint(1, 19)
                                self.foodX = nx * self.width
                                self.foodY = ny * self.height
                        self.food = self.cv.create_rectangle(self.foodX, self.foodY,
                                                             (nx + 1) * self.width, (ny + 1) * self.height,
                                                             fill=self.colorFood, outline=self.colorCV)
                        self.master.update()
                        break
                time.sleep(0.1)
            elif not self.runGame:
                time.sleep(1)
            elif self.runGame and self.gameOver:
                break

    def moveLoop(self):
        xn = self.width
        yn = 0
        while self.t1.is_alive():
            if self.runGame and not self.gameOver:
                if not self.queue.empty():
                    n = self.queue.get()
                    if n == 'Left':
                        xn = -self.width
                        yn = 0
                    elif n == 'Right':
                        xn = self.width
                        yn = 0
                    elif n == 'Up':
                        xn = 0
                        yn = -self.height
                    elif n == 'Down':
                        xn = 0
                        yn = self.height
                    self.currentDirection = n
                tx = self.x[-1]
                ty = self.y[-1]
                self.x[-1] = self.x[0] + xn
                self.y[-1] = self.y[0] + yn
                tempSnake = [self.snake[-1]]
                tempY = [self.y[-1]]
                tempX = [self.x[-1]]
                for i in range(len(self.snake) - 1):
                    tempSnake.append(self.snake[i])
                    tempY.append(self.y[i])
                    tempX.append(self.x[i])
                self.x = tempX
                self.y = tempY
                self.snake = tempSnake
                self.cv.move(self.snake[0], self.x[0] - tx, self.y[0] - ty)
                self.master.update()
                time.sleep(0.2)
            elif not self.runGame:
                time.sleep(1)
            elif self.runGame and self.gameOver:
                break

    def addMovement(self, direction):
        if direction != self.currentDirection:
            if self.currentDirection == 'Left' and direction != 'Right' or \
                    self.currentDirection == 'Right' and direction != 'Left' or \
                    self.currentDirection == 'Up' and direction != 'Down' or \
                    self.currentDirection == 'Down' and direction != 'Up':
                self.queue.put(direction)

    def restart(self):
        for i in self.snake:
            self.cv.delete(i)
        self.cv.delete(self.labelGameOver)
        self.cv.delete(self.food)
        x = self.width * self.startElements
        y = self.height * 2
        self.x = []
        self.y = []
        self.snake = []
        self.queue = SimpleQueue()
        self.currentDirection = 'Right'
        self.runGame = False
        self.gameOver = False
        self.labelGameOver = 0
        self.score = 0
        self.foodX = 10 * self.width
        self.foodY = 10 * self.height
        self.food = self.cv.create_rectangle(self.foodX, self.foodY, self.foodX + self.width,
                                             self.foodY + self.height, fill=self.colorFood, outline=self.colorCV)
        for i in range(self.startElements):
            self.x.append(x - self.width * i)
            self.y.append(y)
            self.snake.append(self.cv.create_rectangle(self.x[i], self.y[i],
                                                       self.x[i] + self.width, self.y[i] + self.height,
                                                       fill=self.color, outline=self.colorCV))
        self.t1 = threading.Thread(target=self.moveLoop)
        self.t2 = threading.Thread(target=self.isFoodReached)
        self.t3 = threading.Thread(target=self.isTailBittenOrBorderReached)
        self.t1.start()
        self.t2.start()
        self.t3.start()

    def autoPilot(self):
        """This method is an AI which calculates the path this object must went in order ot
        reach the food reference defined by two coordinates."""
        pass

    def observeRoute(self):
        pass


if __name__ == '__main__':

    def checkForRestart():
        global snake, t, start
        while snake.gameOver and threading.main_thread().is_alive():
            time.sleep(0.5)
        start.configure(text=' Start ', command=snake.startGame)
        t = threading.Thread(target=updateScore)
        t.start()


    def updateScore():
        global currentScore, start, name
        while not snake.gameOver and threading.main_thread().is_alive():
            currentScore.set(name + ' ' + str(snake.score))
            time.sleep(0.5)
        if threading.main_thread().is_alive():
            start.configure(text='Restart', command=snake.restart)
            tn = threading.Thread(target=checkForRestart)
            tn.start()


    root = Tk()
    root.iconbitmap('C:\\Users\\Dominik Lovetinsky\\Desktop\\Python\\snake.ico')
    root.title('Snake')
    root.configure(bg='blue')

    name = 'Player'
    currentScore = StringVar()
    try:
        name = sys.argv[1]
    except IndexError:
        pass

    snake = Snake(root, startElements=5, colorFood='#4b0082')
    snake.cv.grid(row=0, column=0, columnspan=2)
    snake.cv.configure(highlightthickness=2, highlightbackground='#4b0082')

    pause = Button(root, text=' Pause ', command=snake.pauseGame, bg='#7fffd4', bd=4, font=('JetBrains Mono', 12))
    pause.grid(row=1, column=0, ipadx=snake.width * 3)
    root.bind('<p>', lambda e: snake.pauseGame())

    start = Button(root, text=' Start ', command=snake.startGame, bg='#7fffd4', bd=4, font=('JetBrains Mono', 12))
    start.grid(row=1, column=1, ipadx=snake.width * 3)
    root.bind('<Return>', lambda e: snake.startGame())

    score = Label(root, textvariable=currentScore, font=('JetBrains Mono', 12), bg='#7fffd4', borderwidth=4,
                  relief="raised")
    score.grid(row=2, column=0, columnspan=2)

    t = threading.Thread(target=updateScore)
    t.start()

    root.mainloop()
    # End of Game
    snake.gameOver = True
