class A:
    def fun1(self):
        l = list(map(int, input("Enter list elements: ").split()))
        l.sort()
        print("Ascending :", l)

        l.sort(reverse=True)
        print("Descending :", l)
    
class B:
    def fun1(self):
        super().fun1()
        l = [26, 42, 11, 24, 21, 11]
        uni = []
        dup = []

        for i in range(len(l)):
            j = l[i]
            if j not in uni:
                uni.append(j)
            else:
                dup.append(uni.index(j))
                dup.append(i)

        print("Duplicate index:", dup)

class C(B,A):
    def fun1(self):
        super().fun1()
        n = int(input("Enter a value : "))
        res = 0

        while n > 0:
            digit = n % 10
            res = res * 10 + digit
            n = n // 10

        print("Reversed number : ", res)

obj = C()
obj.fun1()