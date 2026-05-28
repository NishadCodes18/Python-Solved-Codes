1.
t_data = ('A', 'B', 'C')
print("Start:", t_data)

l_temp = list(t_data)
l_temp.insert(1, 'X')
t_data = tuple(l_temp)
print("Insert:", t_data)

t_data = t_data + ('Y', 'Z')
print("Extend:", t_data)

l_temp = list(t_data)
l_temp.reverse()
t_data = tuple(l_temp)
print("Reverse:", t_data)

l_temp = list(t_data)
l_temp[0] = 'a'
t_data = tuple(l_temp)
print("Update (Index 0):", t_data)

l_temp = list(t_data)
l_temp.remove('B')
t_data = tuple(l_temp)
print("Removed(B):", t_data)

del t_data
print("Deleted.")


2.
my_tuple = (10, 20, 30, 20, 40, 10, 50)

seen = set()
duplicates = set()

for item in my_tuple:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print(list(duplicates))


3.
t = (50, 10, 80, 5, 100)
print("Tuple:", t)

print("Min:", min(t))
print("Max:", max(t))
