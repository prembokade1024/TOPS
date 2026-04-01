def palindrome(l):
    length = len(l) // 2
    for i in range(length):
        if l[i] != l[-i - 1]:
            return False
    return True


def sort_asc_desc(l):
    l.sort()
    print("Ascending :", l)

    l.sort(reverse=True)
    print("Descending :", l)


def duplicate(l):
    result = []
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] == l[j]:
                result.append((i, j))
    return result


def reverse_string(s):
    rev = ""
    for i in s:
        rev = i + rev
    return rev

while True:

    menu = """ 
    Press 1 for Palindrome
    Press 2 for Ascending and Descending
    Press 3 for Find duplicates
    Press 4 for Reverse a string
    Press 5 for Exit
    """

    print(menu)

    choice = int(input("Enter your choice : "))

    if choice == 1:
        l = []
        n = int(input("How many elements you want to enter : "))
        for i in range(n):
            num = int(input("Enter element : "))
            l.append(num)

        print("Palindrome :", palindrome(l))

    elif choice == 2:
        l = []
        n = int(input("How many elements you want to enter : "))
        for i in range(n):
            num = int(input("Enter element : "))
            l.append(num)

        sort_asc_desc(l)

    elif choice == 3:
        l = []
        n = int(input("How many elements you want to enter : "))
        for i in range(n):
            num = int(input("Enter element : "))
            l.append(num)

        print("Duplicate indexes :", duplicate(l))

    elif choice == 4:
        s = input("Enter a string : ")
        print("Reverse of string :", reverse_string(s))

    elif choice == 5:
        print("Thank you!!!!!")
        break

    else:
        print("Invalid input")