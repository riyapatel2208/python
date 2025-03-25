import pro12 as f_dtl

def display_menu():
    print("\nFriends Information System")
    print("1. Add Friend")
    print("2. Remove Friend")
    print("3. Update Phone Number")
    print("4. Update GitHub Username")
    print("5. View Friend by Name")
    print("6. View All Friends")
    print("7. Exit \n")

def main():
    while True:
        display_menu()

        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            name = input("Enter new friend's name: ")
            phone = input("Enter phone number: ")
            github = input("Enter GitHub username: ")
            f_dtl.add_friend(name, phone, github)

        elif user_choice == "2":
            name = input("Enter friend's name to remove: ")
            f_dtl.remove_friend(name)

        elif user_choice == "3":
            name = input("Enter friend's name: ")
            new_phone = input("Enter new phone number: ")
            f_dtl.update_phone_number(name, new_phone)

        elif user_choice == "4":
            name = input("Enter friend's name: ")
            new_github = input("Enter new GitHub username: ")
            f_dtl.update_github_username(name, new_github)

        elif user_choice == "5":
            name = input("Enter friend's name: ")
            f_dtl.view_friend_by_name(name)

        elif user_choice == "6":
            f_dtl.view_all_friends()

        elif user_choice == "7":
            print("Exit")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
