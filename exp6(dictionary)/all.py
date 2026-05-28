1.
student = {"name": "ABC", "age": 28}

print("Original Dictionary :")
print(student)

print("Access name:", student["name"])

student["age"] = 17
print("Updated age : ", student["age"])

del student["name"]
print(student)

del student
print("Dictionary deleted.")


2.
dict1 = {"a" : 1, "b" : 2}
dict2 = {"c" : 3, "d" : 4}

new_dict = {**dict1, **dict2}
print("concatenated dictionaries")
print(new_dict)


3,
student = {
    "a" : 10,
    "b" : 20,
    "c" : 10,
    "d" : 30,
    "e" : 20
}

unique_values = set(student.values())
print("unique Values : ")
print(unique_values)
