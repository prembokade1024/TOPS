# d = {1:"hello",2:"python",3:"world",4:"world"}

# print(d)

# print(d.get(1)) # displays the vlaue of a key
# print(d.items()) # displays the items(key : value)

# d.keys() # displays the key
# d.values() # displays the values
# d.update({5:"why",6:"this"}) # adds from back
# print(d) 

# d.pop(1) # removes the item of a given key
# print(d)

# d.popitem() # removes the items from back
# print(d)

# d = {}
# for i in range(1,31):
#     d[i] = i * i

# print(d)

# # occcurence of string
# s = input("Enter a name : ")
# d = {}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

l = [6,8,10]
l1 = [16,18,21,22]
d = {}
for i in range(len(l)):
    d[l[i]] = l1[i]

print(d)
print(len(l))