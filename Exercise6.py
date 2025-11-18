password = "12345"
tries = 0
limit = 5

while tries < limit:
    user_input = input("Enter password: ")

    if user_input == password:
        print("Correct password. Access granted.")
        break
    else:
        tries += 1
        left = limit - tries

        if left > 0:
            print("Wrong password. Attempts left:", left)
        else:
            print("Wrong password. No attempts left. Authorities have been alerted.")
