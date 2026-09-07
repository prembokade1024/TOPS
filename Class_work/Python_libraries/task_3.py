# import requests

# url = "https://jsonplaceholder.typicode.com/posts"
# response = requests.get(url)

# if response.status_code == 200:
#     posts = response.json()
#     for i, post in enumerate(posts[:5], 1):
#         print(f"{i}. {post['title']}")
# else:
#     print("Failed to fetch data")

# 

import matplotlib.pyplot as plt

# Simulated dataset for movie listings
genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi']
movies_count = [14, 8, 11, 4, 7]

# Create a bar chart
plt.figure(figsize=(8, 5))
plt.bar(genres, movies_count, color=['#e63946', '#f4a261', '#2a9d8f', '#264653', '#e9c46a'])

# Add labels and title
plt.xlabel('Movie Genres', fontweight='bold')
plt.ylabel('Number of Movies', fontweight='bold')
plt.title('Current Movies per Genre')

# Display the chart
plt.tight_layout()
plt.show()