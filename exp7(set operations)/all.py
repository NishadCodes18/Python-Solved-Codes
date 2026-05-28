1.
# (1) create
my_set = {1, 2, 3, 4}
print("set : ", my_set)

# (2) Accessing elements using loop
print("\n Accessing elements using loop: ")
for item in my_set:
    print(item)

# (3) Add element
my_set.add(5)
print("\n After adding 5 : ", my_set)

# (4) Update set
my_set.update([6, 7])
print("\n After adding 6 and 7 : ", my_set)

# (5) Remove element
my_set.remove(2)
print("\n After removing 2 : ", my_set)

# (6) Discard element
my_set.discard(10)
print("\n After discarding 10 (no error if not found) : ", my_set)

# (7) Pop element
removed_item = my_set.pop()
print("\n popped element : ", removed_item)
print("\n set after pop : ", my_set)

# (8) Clear set
my_set.clear()
print("\n After clearing the set : ", my_set)


2.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("set 1 : ", set1)
print("set 2 : ", set2)

# 1. intersection
print("\n Intersection : ", set1.intersection(set2))

# 2. union
print("\n union : ", set1.union(set2))

# 3. set difference
print("\n set difference : ", set1.difference(set2))

# 4. symmetric difference
print("\n symmetric difference : ", set1.symmetric_difference(set2))

# 5. clear a set
set1.clear()
print("\n set 1 after clear () : ", set1)


3.# 1. create a set
my_set = {1, 2, 3}
print("Initial set : ", my_set)

# 2. Add a single member
my_set.add(4)
print("\n After adding (4) : ", my_set)

# 3. Remove one item
my_set.remove(2)
print("\n After removing 2 : ", my_set)
