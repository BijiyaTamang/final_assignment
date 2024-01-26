import hashlib
import getpass

file = "data.txt"

def deluser():
    with open(file, 'r') as x:
        data = x.readlines()

    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    
    h = hashlib.new("SHA256")
    h.update(password.encode())
    password_hash = h.hexdigest()

    found = False

    for j, i in enumerate(data):
        name = i.strip().split(':')[0]
        stored_hash = i.strip().split(':')[2]
        if username == name and password_hash == stored_hash:
            del data[j]
            found = True
            break

    if found:
        with open(file, "w") as x:
            x.writelines(data)
        print("User deleted.\n")
    else:
        print("User not found or incorrect password.\n")

    return username, password_hash   

deluser()
