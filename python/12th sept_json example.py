import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'  # The API endpoint
data = {
    "id": 1,
    "title": "Updated Title",  # Updated content
    "body": "This is the updated body of the post",
    "userId": 1
}

response = requests.put(url, json=data)

if response.status_code == 200:
    print("Resource updated successfully!")
    print(response.json())  # Print the updated resource
else:
    print(f"Failed to update resource. Status code: {response.status_code}")
