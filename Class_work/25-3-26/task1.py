# try:
#     n = int(input("Enter number 1 : "))
#     n1 = int(input("Enter nuumber 2 : "))
    
#     print("Addition : ", n+n1)

# except ValueError as e:
#     print(e)
# else:
#     print("Try executed")
# finally:
#     print("Finally executed")

# try:
#     n = int(input("Enter number 1 : "))
#     n1 = int(input("Enter nuumber 2 : "))
    
#     print("Division : ", n / n1)

# except ValueError as e:
#     print(e)

# except  ZeroDivisionError as e:
#     print(e)

# try:
#     l = [74,26,11,32]    
#     n = int(input("Enter index : "))
#     print("Index value : ",l[n])
# except IndexError as e:
#     print(e)

try:
    l = [74,26,11,32]    
    n = int(input("Enter index : "))
    print("Index value : ",l[n])
except:
    print("Invalid input!!")


