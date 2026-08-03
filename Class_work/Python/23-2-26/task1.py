# task_1........................
# s = input("Enter a string : ")
# length = len(s)
# mid = length // 2

# if(length % 2 == 0):
#     print("Middle : ", s[mid-1] + s[mid] + s[mid+1])
# else:
#     print("Middle : ",s[mid])

s = input("Enter a string : ")
rev = ""

for i in s:
    rev = i + rev

print("Reverse of string : ",rev)

# list 
# collection of data type which store multiple vaues in single variable
# denoted by []
# allow duplicates
# orderable
# mutable(changes)

# l = ["helllo", 0 , 10, True, 10.5]
# print(l.append(9)) # adds the elements from back
# print(l.clear()) # clears the whole list
# print(l.copy()) # copies the whole list
# print(l.count(1)) # counts the element present in list with their times


