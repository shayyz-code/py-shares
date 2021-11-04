# nanii?

def main():

# initial values - email & password (usually environment variables)

    email = "admin0001@gmail.com"
    psw = "admin%0001"

    def user_login ():
        for i in range(3):
            email_input = input("Enter user email>>>:")
            psw_input = input("Enter password:")

            if email_input == email and psw_input == psw:
                print(f"Your account(( {email} )) is successfully logged in.\n\n")
                print(f"Choose a function!\n)Add user\n)Modify account info\n)Remove account\n\nEnter function number here (1 or 2 or 3)>>>")
                break
            else:
                print(f"Wrong gmail or password! You can try 3 times. {i}\3")
    
    user_login()

if __name__ == "__main__":
    main()

