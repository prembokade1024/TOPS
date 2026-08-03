# task_1...............
# l = []
# ev = []
# od = []

# for i in range(1,31):
#     l.append(i)
#     if i % 2 == 0:
#         ev.append(i)
#     else:
#         od.append(i)

# print(l)
# print(ev)
# print(od)

# task_2...........
# l = [1,2,3,4,1,2]
# uni = []

# for i in l:
#     if i not in uni:
#         uni.append(i)
# print(uni)

# task_3.....................
# l = [1,2,3,2,1]
# length = len(l) // 2
# is_palindrome = True
# for i in range(length):
#     if l[i] != l[-1 -i]:
#         is_palindrome = False
#         break
# print(is_palindrome)

# task_4..................
# l = [1,2,3,2,1]
# left = 0
# right = len(l)-1

# ans = "Yes"+

# while(left < right):
#     if l[left] == l[right]:
#         left+=1
#         right-=1
#         continue
#     else:
#         ans = "No"
#         break
# print(ans)


l = [1,2,3,2,4]
left = 0
right = len(l)-1

ans = "Yes"
while(left < right):
    if l[left] != l[right]:
        ans = "No"
        break
    left+=1
    right-=1

print(ans)

