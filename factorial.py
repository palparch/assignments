# 5! = 1*2*3*4*5


num = int(input("Number daalo ji: "))

factorial = 1

for i in range(1, num+1):
    factorial *= i

print(factorial)
