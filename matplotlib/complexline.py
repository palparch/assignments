import matplotlib.pyplot as plt

x = range(0,6)
y = range(20,46,5)

#plt.plot(x, y, linestyle='--', marker='o', markersize=8)
#plt.grid()
#plt.xlabel("Month")
#plt.ylabel("Sales")
#plt.legend("Sales")
#plt.show()


mon = ['Jan','Feb','Mar','Apr','May']
sales = [20,35,30,45,50]
expenses = [15,25,28,32,40]

plt.plot(mon, sales, marker='o', color='cyan', markersize=10, label="Sales")
plt.plot(mon, expenses, marker='^', linestyle="--", color='green', markersize=8, label="Expenses")
plt.legend()
plt.ylabel("Sales & expenses")
plt.show()
