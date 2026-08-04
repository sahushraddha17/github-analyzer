
import requests


def fetch_github_profile(username):
    """Fetch GitHub profile data using the GitHub API."""
    url = f"https://api.github.com/users/{username}"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response
        elif response.status_code == 404:
            print("❌ User not found.")
            return None
        else:
            print(f"❌ Error: Received status code {response.status_code}")
            return None
            
    except requests.exceptions.RequestException:
        print("❌ No Internet Connection or Network Error:")
        return None
