import numpy as np


def factorial(x: int):
    return x * factorial(x-1) if x > 1 else 1


x = np.arange(1, 10)
sum_ = 0

for i in x:
    sum_ += (i + 1) / (factorial(i))


print(sum_)
print(factorial(20))
