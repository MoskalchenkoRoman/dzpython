import random
list = [random.randint(0,6) for i in range (10)]
print(list)
new_list = []
nls = []
for char in set(list):
    if list.count(char) < 2:
        new_list.append(char)
    else:
        nls.append(char)
print(new_list)
print(nls)
print(set(list))