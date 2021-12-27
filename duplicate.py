list1 = [7,5,7,0,8,-5,-88,53,79,-2]

def remove_duplicate(list):
    list2 = []
    for num in list1:
        if num not in list2:
            list2.append(num)
    return list2

print(remove_duplicate(list1))

list1.sort()
print(list1)

