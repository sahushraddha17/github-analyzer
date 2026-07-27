import requests

username = input("Enter GitHub username: ")

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

print(response.status_code)

data = response.json()

print("Name:", data["name"])
print("Username:", data["login"])
print("Bio:", data["bio"])
print("Followers:", data["followers"])
print("Following:", data["following"])
print("Public Repositories:", data["public_repos"])
print("Created Date:", data["created_at"])torvalds