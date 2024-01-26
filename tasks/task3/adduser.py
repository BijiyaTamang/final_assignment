import hashlib
import getpass

userid = {}
file = "data.txt"
h = hashlib.new("SHA256")

def adduser():

    with open(file, 'r') as x:
        data = x.readlines()
        username = input("Enter new username: ")
        real_name = input("Enter real name: ")
        password = getpass.getpass("Enter password: ")
        
        h.update(password.encode())
        password_hash = h.hexdigest()
        
        for i in data:
            name = i.strip().split(':')[0]
            if username == name:
                print("Cannot add. Most likely username already exists.\n")  
                return 
        
        if username == real_name:
            print("Username and real name cannot be the same.\n")   
            return  

        data.append(f"{username}:{real_name}:{password_hash}\n")
        
        with open(file, "w") as x:
            x.writelines(data)
            print("User Created.\n")

    return username, real_name, password_hash 

adduser()
