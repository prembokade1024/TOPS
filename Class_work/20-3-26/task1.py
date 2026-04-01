# import math

# print(math.factorial(5))
# print(math.sqrt(6))
# print(math.floor(3.65))
# print(math.acos(0.55))
# print(math.asin(0.44))

# x = lambda a,b,c : a + b + c
# print(x(15,65,32))

# x = lambda n : n * n
# print(x(6))

l = ["apple","banana","cherry","kiwi","mango"]

newlist = list({x for x in l if "a" not in x})

print(newlist)

