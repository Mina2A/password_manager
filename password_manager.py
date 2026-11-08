from cryptography.fernet import Fernet


'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''



def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key




key = load_key() 
fer = Fernet(key)






def view():
    with open("passwords.txt", "r") as f:
        for line_number, line in enumerate(f, 1):
            data = line.rstrip("\r\n")
            if not data:
                continue

            user, separator, passw = data.partition("|")
            if not separator:
                print(f"Skipping malformed entry on line {line_number}: expected '|' separator.")
                continue

            print(repr(data))

            print("user: ",user," | Password:",fer.decrypt(passw.encode()).decode())



    
def add():
    name = input(" account name: ")
    pwd = input(" password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" +fer.encrypt(pwd.encode()).decode() + "\n")
        


while True:
    mode = input("would you add or view your password? (add/view) ,prass (q) to quit: ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
          add()
    else:
        print("Invalid option.")
        continue
