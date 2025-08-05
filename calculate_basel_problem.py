def prime_numbers(num):
    prime_list = []
    for i in range(1, num):
        prime_list.append(i**2)

    return prime_list

#print(prime_numbers(5))


def basel_problem(prime_list, num_limit):
    answer = 0
    i = 0

    while i < num_limit:
        answer += 1/int(prime_list[i-1])
        i+=1

    return answer

num_limit = int(input("till what number? :"))


print(basel_problem(prime_numbers(num_limit), num_limit))
    
