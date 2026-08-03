# import requests

# def get_stock_data():
#     url = "https://jsonplaceholder.typicode.com/posts"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         print(data)
#     else:
#         return None

# get_stock_data()

l = [1,2,3,4,5]

for i in range(len(l)):
    l[i] += 5

print(l)
