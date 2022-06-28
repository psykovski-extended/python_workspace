from __future__ import division
from numba import cuda
import numpy
import math


@cuda.jit
def my_kernel(io_array, obj):
    pos = cuda.grid(1)
    if pos < io_array.size:
        io_array[pos] *= 2  # do the computation


# Host code
data = numpy.ones(256, numpy.int)
threadsperblock = 256
blockspergrid = math.ceil(data.shape[0] / threadsperblock)
print(blockspergrid)
my_kernel[blockspergrid, threadsperblock](data)
print(data)
