from utils import get_username, save_history
from github_api import fetch_github_profile
from display import display_profile
def main():
    username = get_username()
    response = fetch_github_profile(username)
    if response is not None:
        save_history(username,"Success")
        display_profile(response)
    else:
        save_history(username,"Failed")
    
if __name__ == "__main__":
    main()