def add_friend(name, phone, github):
    with open("friends.txt", 'a') as file:
        file.write(f"{name},{phone},{github}\n")
    print(f"Friend {name} added.")

def remove_friend(name):
    found = False
    with open("friends.txt", 'r') as file:
        lines = file.readlines()

    with open("friends.txt", 'w') as file:
        for line in lines:
            if not line.startswith(name + ","):
                file.write(line)
            else:
                found = True

    if found:
        print(f"Friend {name} removed.")
    else:
        print(f"Friend {name} not found.")

def update_phone_number(name, new_phone):
    updated = False
    with open("friends.txt", 'r') as file:
        lines = file.readlines()

    with open("friends.txt", 'w') as file:
        for line in lines:
            if line.startswith(name + ","):
                details = line.split(",")
                details[1] = new_phone
                file.write(",".join(details))
                updated = True
            else:
                file.write(line)

    if updated:
        print(f"Phone number of {name} updated.")
    else:
        print(f"Friend {name} not found.")

def update_github_username(name, new_github):
    updated = False
    with open("friends.txt", 'r') as file:
        lines = file.readlines()

    with open("friends.txt", 'w') as file:
        for line in lines:
            if line.startswith(name + ","):
                details = line.split(",")
                details[2] = new_github
                file.write(",".join(details) + "\n")
                updated = True
            else:
                file.write(line)

    if updated:
        print(f"GitHub username of {name} updated.")
    else:
        print(f"Friend {name} not found.")

def view_friend_by_name(name):
    found = False
    with open("friends.txt", 'r') as file:
        for line in file:
            if line.startswith(name + ","):
                print(line.strip())
                found = True

    if not found:
        print(f"Friend {name} not found.")

def view_all_friends():
    with open("friends.txt", 'r') as file:
        for line in file:
            print(line.strip())

