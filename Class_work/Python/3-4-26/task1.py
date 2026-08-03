# class A:

#     def fun1(self):
#         n = int(input("Enter a value : "))
#         res = 0

#         while n > 0:
#             digit = n % 10
#             res = res * 10 + digit
#             n = n // 10

#         print("Reversed number : ", res)


# class B(A):

#     def fun2(self):
#         l = list(map(int, input("Enter list elements: ").split()))
#         l.sort()
#         print("Ascending :", l)

#         l.sort(reverse=True)
#         print("Descending :", l)
    
# class C(B):

#     def fun3(self):
#         l = list(map(int, input("Enter list elements: ").split()))
#         l.sort()
#         print("Ascending :", l)

#         l.sort(reverse=True)
#         print("Descending :", l)

# obj = C()
# obj.fun1()
# obj.fun2()
# obj.fun3()

# class A:

#     def fun1(self):
#         n = int(input("Enter a value : "))
#         res = 0

#         while n > 0:
#             digit = n % 10
#             res = res * 10 + digit
#             n = n // 10

#         print("Reversed number : ", res)


# class B(A):

#     def fun2(self):
#         l = list(map(int, input("Enter list elements: ").split()))
#         l.sort()
#         print("Ascending :", l)

#         l.sort(reverse=True)
#         print("Descending :", l)
    
# class C(A):

#     def fun3(self):
#         l = list(map(int, input("Enter list elements: ").split()))
#         l.sort()
#         print("Ascending :", l)

#         l.sort(reverse=True)
#         print("Descending :", l)

# obj1 = C()
# obj2 = B()
# obj1.fun1()
# obj2.fun2()
# obj1.fun3()


# class A:

#     def fun1(self):
#         n = int(input("Enter a value : "))
#         res = 0

#         while n > 0:
#             digit = n % 10
#             res = res * 10 + digit
#             n = n // 10

#         print("Reversed number : ", res)


# class B(A):

#     def fun2(self):
#         l = list(map(int, input("Enter list elements: ").split()))
#         l.sort()
#         print("Ascending :", l)

#         l.sort(reverse=True)
#         print("Descending :", l)
    
# class C(B,A):

#     def fun3(self):
#         l = list(map(int, input("Enter list elements: ").split()))
#         l.sort()
#         print("Ascending :", l)

#         l.sort(reverse=True)
#         print("Descending :", l)

# obj = C()
# obj.fun1()
# obj.fun2()
# obj.fun3()

class A:

    def fun1(self):
        n = int(input("Enter a value : "))
        res = 0

        while n > 0:
            digit = n % 10
            res = res * 10 + digit
            n = n // 10

        print("Reversed number : ", res)


class B(A):

    def fun2(self):
        l = list(map(int, input("Enter list elements: ").split()))
        l.sort()
        print("Ascending :", l)

        l.sort(reverse=True)
        print("Descending :", l)
    
class abc(A,B):

    def fun2(self):
        l = list(map(int, input("Enter list elements: ").split()))
        l.sort()
        print("Ascending :", l)

        l.sort(reverse=True)
        print("Descending :", l)

class C(B,A,abc):

    def fun3(self):
        l = list(map(int, input("Enter list elements: ").split()))
        l.sort()
        print("Ascending :", l)

        l.sort(reverse=True)
        print("Descending :", l)

obj1 = C()
obj.fun1()
obj.fun2()
obj.fun3()