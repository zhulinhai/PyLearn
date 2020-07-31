import numpy as np

# Generate some random	data 
data = np.random.randn(2, 3)

print(data)

print(data * 10)

print(data + data)

print(data.shape)

print(data.dtype)

data1 = [6, 7.5, 8, 0, 1]

arr1 = np.array(data1)

print(arr1)

data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)

print(arr2)

print(arr2.ndim)
print(arr2.shape)

print(arr1.dtype)
print(arr2.dtype)

print(np.zeros(10))
print(np.zeros((3,6)))

print(np.empty((2,3,2)))

print(np.arange(15))

arr1 = np.array([1,2,3], dtype=np.float64)

print(arr1)

arr3d =	np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
print(arr3d[0])

# 基本的索引和切片
arr = np.arange(10)
print(arr)

print(arr[5])

print(arr[5:8])
arr[5:8] = 12
print(arr)

# 切片索引
arr2d = [[1,2,3],[4,5,6],[7,8,9]]
print(arr2d[:2])
print(arr2d[1:])

# 花式索引
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i

print(arr)

print(arr[[4, 3, 0, 6]])


arr = np.random.randn(6, 3)
print(arr)

print(np.dot(arr.T, arr))

# 通用函数
arr = np.arange(10)
print(arr)

print(np.sqrt(arr))

print(np.exp(arr))

x = np.random.randn(8)

y = np.random.randn(8)

print(x)
print(y)

print(np.maximum(x, y))

arr = np.random.randn(7) * 5
print(arr)

remainder, whole_part =	np.modf(arr)
print(remainder)
print(whole_part)

points = np.arange(-5, 5, 0.01)

xs, ys = np.meshgrid(points, points)

print(ys)

z = np.sqrt(xs ** 2 + ys ** 2)
print(z)

import matplotlib.pyplot as plt

plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
plt.title("Image	plot	of	$\sqrt{x^2	+	y^2}$	for	a	grid	of	values") 