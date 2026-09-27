import matplotlib.pyplot as plt

marks = [18, 19, 19, 20, 20, 20, 21, 21, 22, 23]

plt.hist(marks, bins=[18, 19, 20, 21, 22, 23])
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Marks Distribution")
plt.show()
