from datetime import datetime
def get_username():
    """Take GitHub username from the user."""
    return input("Enter GitHub username: ")

def save_history(username, status):
    """Save the searched username to history.txt with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    
    with open("history.txt", "a") as file:
        file.write(f"[{timestamp}] {status} | {username}\n")
        
        
      
        