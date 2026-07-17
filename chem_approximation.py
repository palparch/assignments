import time

y = input("what is the actual value?")
# x is unknown 

x = 0
i = 0
z = 0

while z != y:
    z = (0.001 * (1-x))**0.5
    
    x+=0.1
    i+=1

    print("x is: ", x)
    print("z is: ", z)
    print("\n")

    time.sleep(2.5)

print(z)
print("number of steps taken: ", i)
