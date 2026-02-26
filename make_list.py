nums = input("Enter a sequence of numbers: ")
raw_list = list(nums)

def check_if_int(num):
    try:
        num1 = int(num)
    except:
        return "false"



def make_int_list(list1):
    num_list = []
    for i in range(0, len(list1)):
        if list1[i].isdigit() or list1[i] == ".":
            if len(num_list) == 0:
                num_list.append(str(list1[i]))
            else:
                num_list[-1] += str(list1[i])
        else:
            if list1[i-1].isdigit():
                num_list.append("")
            else: 
                continue

    for i in range(0, len(num_list)):
        if check_if_int(num_list[i]) == "false":
            num_list[i] = float(num_list[i])
        else:
            num_list[i] = int(num_list[i])

    return num_list

final_list = make_int_list(raw_list)
print(final_list)
