from utils import get_username
from github_api import fetch_github_profile
from display import display_profile
def main():
    username = get_username()
    response = fetch_github_profile(username)
    if response is not None:
        display_profile(response)
    
if __name__ == "__main__":
    main()