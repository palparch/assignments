import matplotlib.pyplot as plt

x = ['Jan', 'Feb', 'Mar', 'Apr']
y = [30, 50, 80, 50]

plt.bar(x,y)
plt.plot(x,y, marker='*', markersize=10, color='green')
plt.show()
