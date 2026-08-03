date = int(input("Enter birth date :  "))
month = int(input("Enter birth month :  "))
year = int(input("Enter birth year :  "))

c_year = 2026
c_date = 28
c_month = 1
total_month = 12

print("Year : ", c_year-year)
print("Month : ", (total_month-month)+c_month)
print("Days : ", c_date-date)