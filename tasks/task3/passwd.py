import hashlib
import getpass

userid = {}
file = "data.txt"

def passwd():
    line_num = 0
    found = False
    data = []
    new_password_hash = ''
    confirmation_hash = ''
    new_line = ""

    with open(file, 'r') as x:
        data = x.readlines()

    username = input("Username: ")
    password = getpass.getpass("Current Password: ")
    h = hashlib.new("SHA256")
    h.update(password.encode())
    password_hash = h.hexdigest()

    for n, i in enumerate(data, start=1):
        name, realname, passwd = i.strip().split(':')

        if username == name:
            if password_hash == passwd:
                found = True
                new_password = getpass.getpass("New Password: ")
                h = hashlib.new("SHA256")
                h.update(new_password.encode())
                new_password_hash = h.hexdigest()

                confirmation = getpass.getpass("Confirm Password: ")
                h = hashlib.new("SHA256")
                h.update(confirmation.encode())
                confirmation_hash = h.hexdigest()

                if new_password_hash != confirmation_hash:
                    print("Password does not match!\n")
                    return

                new_line = f"{username}:{realname}:{new_password_hash}\n"
                line_num = n
                print("Password Changed.\n")
                break

    if found:
        data[line_num - 1] = new_line
        with open(file, 'w') as x:
            x.writelines(data)
    else:
        print("Username or Password does not match!\n")

    return username, new_password_hash

passwd()
