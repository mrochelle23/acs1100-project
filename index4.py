my_file = open('data.txt', 'r')
data = my_file.read()
account_1 = "aman,1234,Andy Allman,1000".split(",")
account_2 = "betho,pa$$word,Beth Beto,2000".split(",")
account_3 = "camcam,default,Cameron Clay,3000".split(",")

def display(account_1, account_2, account_3):
    while True:
        username = input("Username: ")
        password = input("Password: ")
        if username == account_1[0] and password == account_1[1]:
            print("Name: Andy Allman")
            print("Balance: 1000.0")
            break
        elif username == account_2[0] and password == account_2[1]:
            print("Name: Beth Beto")
            print("Balance: 2000.0")
            break
        elif username == account_3[0] and password == account_3[1]:
            print("Name: Cameron Clay")
            print("Balance: 3000.0")
            break
        else:
            print("Username and password don't exist")
            continue

def login(username, password):
    
    return username == {
            "username":"aman",
            "username":"betho",
            "username":"camcam"
    } and password == {
        "password":"1234",
        "password":"pa$$word",
        "password":"default"
    }

display(account_1, account_2, account_3)
login('username', 'password')