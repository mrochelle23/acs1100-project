
# Open and read the data file
with open('data.txt', 'r') as my_file:
    data = my_file.readlines()

# Process each line into a list of accounts
accounts = [line.strip().split(',') for line in data]

def display(accounts):
    while True:
        username = input("Username: ")
        password = input("Password: ")
        
        # Find the account that matches the username and password
        account_found = False
        for account in accounts:
            if username == account[0] and password == account[1]:
                print(f"Name: {account[2]}")
                print(f"Balance: {account[3]}")
                account_found = True
                break
        
        if account_found:
            break
        else:
            print("Username and password don't exist")
            continue

def login(username, password, accounts):
    # Check if the username and password match any account
    for account in accounts:
        if account[0] == username and account[1] == password:
            return True
    return False

# Run display function
display(accounts)

# Example of using the login function
print(login('aman', '1234', accounts))

