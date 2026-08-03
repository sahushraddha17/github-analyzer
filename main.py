from urllib import response

import requests


def get_username():
    """Take GitHub username from the user."""
    return input("Enter GitHub username: ")


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


def display_profile(response):
    """Display GitHub profile information."""
    if response is not None:
        profile_data = response.json()

        print("\n===== GitHub Profile =====")
        print(f"Username: {profile_data['login']}")
        print(f"Name: {profile_data.get('name', 'N/A')}")
        print(f"Bio: {profile_data.get('bio', 'N/A')}")
        print(f"Followers: {profile_data['followers']}")
        print(f"Following: {profile_data['following']}")
        print(f"Public Repositories: {profile_data['public_repos']}")
        print(f"Created Date: {profile_data['created_at']}")
    else:
        print("❌ User not found or an error occurred.")


def main():
    username = get_username()
    response = fetch_github_profile(username)
    if response is not None:
        display_profile(response)
    


if __name__ == "__main__":
    main()