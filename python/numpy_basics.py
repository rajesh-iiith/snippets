import numpy

'''
NumPy provides 
	1. a multidimensional array object, 
	2. various derived objects (such as masked arrays and matrices), 
	3. and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.
'''
'''
Everything revolves around an ndarry object.
Differences between NumPy arrays and the standard Python sequences:
	1. NumPy arrays have a fixed size at creation, unlike Python lists (which can grow dynamically).
	2. The elements in a NumPy array are all required to be of the same data type.
	3. NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of data.
'''
'''
For detailed documentation go to 
http://docs.scipy.org/doc/numpy/reference/
'''	

# numpy functions can be called over a python list
numbers = [1,2,3,4,5]
print numpy.mean(numbers)
print numpy.median(numbers)
print numpy.std(numbers)

# arrays in numpy
#  1D
array1D = numpy.array([34, 21, 32, 45, 23], int)
print array1D, array1D[1], array1D[:1]
#  2D
array2D = numpy.array([[34, 21, 32, 45, 23],[21, 23, 55, 64, 11]] , int)
print array2D, array2D[0][0], array2D[:,1], array2D[0,:]

#array arithmatics
#  1D
array_1 = numpy.array([1, 2, 3], float)
array_2 = numpy.array([5, 2, 6], float)
print array_1 + array_2
print array_1 - array_2
print array_1 * array_2
#  2D
array_1 = numpy.array([[1, 2], [3, 4]], float)
array_2 = numpy.array([[5, 6], [7, 8]], float)
print array_1 + array_2
print array_1 - array_2
#note: this just print the multiplication of corresponding matrix elements
print array_1 * array_2

#some common mathematical operations
print numpy.mean(array1D);
print numpy.mean(array2D);

#dot product
array_1 = numpy.array([1, 2, 3], float)
array_2 = numpy.array([[6], [7], [8]], float)
print numpy.dot(array_1, array_2)



