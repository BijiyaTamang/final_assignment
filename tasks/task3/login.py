import hashlib
import getpass

file = "data.txt"

def login():
    with open(file, 'r') as x:
        data = x.readlines()

    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    
    h = hashlib.new("SHA256")
    h.update(password.encode())
    password_hash = h.hexdigest()

    found = False  

    for i in data:
        name, _, passwd = i.strip().split(':')
        if username == name and password_hash == passwd:
            found = True
            print("Access granted.\n")
            break
                
    if not found:  
        print("Access denied\n")

    return username, password_hash  

login()
