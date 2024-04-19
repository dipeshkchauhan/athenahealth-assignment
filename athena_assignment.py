import requests
import json

###############################################################################
# Script Purpose:
#   This script fetches data from a specified endpoint and parses it into a
#   suitable data structure. It then prints the number of posts returned by
#   that endpoint.
#
# Date: 18-04-1994
# Author: Dipesh Kumar
# Version: 1.0
###############################################################################

# Function to count the number of posts
def count_posts(posts):
    # Check if posts data is available
    if posts:
        # Return the number of posts (length of the list)
        return len(posts)
    else:
        # If no data available, return 0
        return 0

# Fetching data from the URL
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

# Parsing the JSON data
if response.status_code == 200:
    data = response.json()

    # Printing the parsed data
    print("Fetched data:")
    print(data[:5])  # printing first 5 posts for demonstration

    # Count the number of posts
    num_posts = count_posts(data)
    print("Number of posts:", num_posts)

else:
    print("Failed to fetch data. Status code:", response.status_code)
