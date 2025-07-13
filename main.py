def n_list_creator():
    req_nums = int(input("how many numbers do you want to compare?: "))
    nums_list = []
    for i in range(0, req_nums):
        new_num = int(input("enter your number: "))
        nums_list.append(new_num)

    return nums_list
    print(nums_list)

def compare_nums(nums_list):
    #nums_list = n_list_creator()

    print(nums_list[0])
    print(nums_list[1])
    print(nums_list[2])
    #print(nums_list[3])

    for i in range(0, len(nums_list)):
        if nums_list[i] > nums_list[i-1]:
            great_num = nums_list[i]
        else:
            great_num = nums_list[i-1]

    print(great_num)

compare_nums(n_list_creator())
