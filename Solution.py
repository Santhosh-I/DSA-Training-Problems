import matplotlib.pyplot as plt

midpoints = [25, 35, 45, 55]
frequency = [4, 9, 12, 5]

plt.plot(midpoints, frequency, marker="o")

plt.xlabel("Age Midpoint")
plt.ylabel("Frequency")
plt.title("Frequency Polygon of Employee Ages")
plt.grid(True)
plt.show()