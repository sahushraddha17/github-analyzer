from utils import get_username, save_history
from github_api import fetch_github_profile
from display import display_profile


def compare_profiles(profiles):
    """Compare selected GitHub profiles."""

    print("\n========================================")
    print("        PROFILES TO COMPARE")
    print("========================================")

    # Display complete profile information
    for profile in profiles:
        display_profile(profile)

    # Convert API responses into dictionaries
    profile_data = [profile.json() for profile in profiles]

    print("\n========================================")
    print("        PROFILE COMPARISON")
    print("========================================")

    # Table Header
    print(f"\n{'Metric':<20}", end="")

    for profile in profile_data:
        print(f"{profile['login']:<20}", end="")

    print()

    print("-" * (20 + 20 * len(profile_data)))

    # Followers
    print(f"{'Followers':<20}", end="")

    for profile in profile_data:
        print(f"{profile['followers']:<20}", end="")

    print()

    # Repositories
    print(f"{'Repositories':<20}", end="")

    for profile in profile_data:
        print(f"{profile['public_repos']:<20}", end="")

    print()


def main():

    while True:

        print("\n========================================")
        print("           GITHUB ANALYZER")
        print("========================================")

        print("\nWhat would you like to do?\n")

        print("1. View GitHub Profile")
        print("   → View data of one GitHub user.\n")

        print("2. Compare GitHub Profiles")
        print("   → Compare 2 or 3 GitHub users.\n")

        print("3. View Search History")
        print("   → View your previous searches.\n")

        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        # ========================================
        # OPTION 1: VIEW ONE PROFILE
        # ========================================

        if choice == "1":

            username = get_username()

            response = fetch_github_profile(username)

            if response is not None:

                save_history(username, "SUCCESS")
                display_profile(response)

            else:

                save_history(username, "FAILED")

        # ========================================
        # OPTION 2: COMPARE PROFILES
        # ========================================

        elif choice == "2":

            print("\n========================================")
            print("       COMPARE GITHUB PROFILES")
            print("========================================")

            print("\nHow many profiles do you want to compare?")

            print("1. Compare 2 profiles")
            print("2. Compare 3 profiles")

            compare_choice = input("\nEnter your choice: ").strip()

            # ========================================
            # COMPARE 2 PROFILES
            # ========================================

            if compare_choice == "1":

                username1 = input(
                    "\nEnter first GitHub username: "
                ).strip()

                username2 = input(
                    "Enter second GitHub username: "
                ).strip()

                response1 = fetch_github_profile(username1)
                response2 = fetch_github_profile(username2)

                if response1 is not None and response2 is not None:

                    save_history(username1, "SUCCESS")
                    save_history(username2, "SUCCESS")

                    profiles = [
                        response1,
                        response2
                    ]

                    compare_profiles(profiles)

                else:

                    print("\n❌ Could not fetch both profiles.")

            # ========================================
            # COMPARE 3 PROFILES
            # ========================================

            elif compare_choice == "2":

                username1 = input(
                    "\nEnter first GitHub username: "
                ).strip()

                username2 = input(
                    "Enter second GitHub username: "
                ).strip()

                username3 = input(
                    "Enter third GitHub username: "
                ).strip()

                response1 = fetch_github_profile(username1)
                response2 = fetch_github_profile(username2)
                response3 = fetch_github_profile(username3)

                if (
                    response1 is not None
                    and response2 is not None
                    and response3 is not None
                ):

                    save_history(username1, "SUCCESS")
                    save_history(username2, "SUCCESS")
                    save_history(username3, "SUCCESS")

                    profiles = [
                        response1,
                        response2,
                        response3
                    ]

                    compare_profiles(profiles)

                else:

                    print("\n❌ Could not fetch all three profiles.")

            else:

                print(
                    "\n❌ Currently, you can compare "
                    "only 2 or 3 profiles."
                )

        # ========================================
        # OPTION 3: VIEW HISTORY
        # ========================================

        elif choice == "3":

            print(
                "\n🚧 Search history viewer "
                "is coming next!"
            )

        # ========================================
        # OPTION 4: EXIT
        # ========================================

        elif choice == "4":

            print(
                "\nThank you for using "
                "GitHub Analyzer! 👋"
            )

            break

        # ========================================
        # INVALID CHOICE
        # ========================================

        else:

            print("\n❌ Invalid choice.")
            print("Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()