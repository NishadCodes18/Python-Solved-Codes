1. Basic Array Operations (NumPy)
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Multiplication:", a * b)
print("Mean of a:", np.mean(a))
print("Sum of b:", np.sum(b))


🔹 2. Matrix Multiplication
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

result = np.dot(A, B)
print("Matrix Multiplication:\n", result)


🔹 3. Plot a Simple Line Graph (Matplotlib)
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


🔹 4. Plot Sine Wave (NumPy + Matplotlib)
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("Angle")
plt.ylabel("sin(x)")
plt.show()


🔹 5. Bar Chart
import matplotlib.pyplot as plt

students = ["A", "B", "C", "D"]
marks = [85, 90, 78, 92]

plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()


🔹 6. Histogram
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)

plt.hist(data, bins=30)
plt.title("Histogram")
plt.show()


🔹 7. Scatter Plot
import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()


🔹 8. 2D Random Data Visualization
import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(10, 10)

plt.imshow(data)
plt.title("2D Heatmap")
plt.colorbar()
plt.show()


🔹 9. Save Plot as Image
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [4, 5, 6]

plt.plot(x, y)
plt.savefig("graph.png")


🔹 10. Real-Life Example: Temperature Analysis
import numpy as np
import matplotlib.pyplot as plt

days = np.arange(1, 8)
temp = np.array([30, 32, 31, 29, 35, 36, 34])

plt.plot(days, temp, marker='o')
plt.title("Weekly Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.show()



For Practice 
1. Array Creation & Statistics
Program:
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))


🔹 2. Element-wise Operations
Program:
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Multiplication:", a * b)


🔹 3. Matrix Addition
Program:
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix Addition:\n", A + B)


🔹 4. Generate Even Numbers & Plot
Program:
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 2)
y = x**2

print("X:", x)
print("Y:", y)

plt.plot(x, y)
plt.show()


🔹 5. Sine Wave Visualization
Program:
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3.14, 5)
y = np.sin(x)

print("X:", x)
print("sin(X):", y)

plt.plot(x, y)
plt.show()


🔹 6. Bar Chart – Student Marks
Program:
import matplotlib.pyplot as plt

students = ["A", "B", "C"]
marks = [75, 85, 90]

print("Students:", students)
print("Marks:", marks)

plt.bar(students, marks)
plt.show()


🔹 7. Histogram of Random Data
Program:
import numpy as np
import matplotlib.pyplot as plt

data = np.array([1,2,2,3,3,3,4,4,5])

print("Data:", data)

plt.hist(data)
plt.show()


🔹 8. Scatter Plot
Program:
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])
y = np.array([5,4,3,2,1])

print("X:", x)
print("Y:", y)

plt.scatter(x, y)
plt.show()


🔹 9. Identity Matrix
Program:
import numpy as np

I = np.eye(3)
print("Identity Matrix:\n", I)


🔹 10. Random Numbers & Mean
Program:
import numpy as np

data = np.random.randint(1, 10, 5)

print("Random Data:", data)
print("Mean:", np.mean(data))
