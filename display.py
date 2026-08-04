
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