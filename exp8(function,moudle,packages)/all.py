1.def calculate(text):
    uppercase = 0
    lowercase = 0
    for char in text:
        if char.isupper():
            uppercase += 1
        if char.islower():
            lowercase += 1

    print("uppercase letters :", uppercase)
    print("lowercase letters :", lowercase)

text = input("enter a string in uppercase and lowercase letters: ")
calculate(text)


2.import math

def calculate(r):
    area = math.pi * r * r
    circumference = 2 * math.pi * r

    print("area : ", round(area, 4))
    print("circumference : ", round(circumference, 4))

r = float(input("enter radius: "))
calculate(r)


3.import numpy as np
import random as r

num_random = [r.randint(10, 30) for _ in range(6)]
print("Random module integers : ", num_random)


4.def college_name():
    return "MIT WPU, Kothrud"
