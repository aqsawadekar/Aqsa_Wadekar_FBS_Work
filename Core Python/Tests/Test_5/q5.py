l1 = [14, 19, 10, 4]
l2 = [21, 2, 18, 6]

l3 = []

for i in l1:
    if i not in l3:
        l3.append(i)

for i in l2:
    if i not in l3:
        l3.append(i)

print("Union of list is: ", l3)