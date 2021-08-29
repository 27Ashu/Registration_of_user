import re

#regular expression to validate the user id provided
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

#Registration of the new user
def User_Registration():

    # input the user name nd check weather it is valid ar not
    user_name = str(input("Enter the username\n"))
    if (re.search(regex,user_name)):
        f = open("registration_details.txt", 'r')
        info = f.read()
        if user_name in info:
            print("User name already available, go for login or forgot password")
            User_options()
            return
        f.close()
    else:
        print("invalid UserName")
        return
    # Checking the Entered password is valid or not
    password = str(input("Enter the password\n"))
    X = True
    while X:
        if (len(password) < 5 or len(password) > 16):
            print("Password length should be between 5 to 16")
            break
        elif not re.search("[a-z]", password):
            print("password should contain lower cases")
            break
        elif not re.search("[A-Z]", password):
            print("password should contain atleast one uppercase")
            break
        elif not re.search("[0-9]", password):
            print("password should contain atleast one digit")
            break
        elif not re.search("[@#$]", password):
            print("password must have a atleast one special character")
            break
        else:
            print("valid password")
            X = False
            #return password
    #Successful copletion of user registration
    if (X == False):
        print("Registration Success go to login page")
    #writing the user details to the file
    f = open("registration_details.txt", 'w')
    info = info + " " + user_name + " " + password
    f.write(info)
    f.close()
    User_options()

#method to get the user requested password based on the info provided
def Forget_password():
    usr_name = str(input("Enter UserName: "))
    f = open("registration_details.txt", 'r')
    info = f.read()
    info = info.split()
    if usr_name in info:
        index = info.index(usr_name) + 1
        usr_password = info[index]
        print(usr_name + " ur password is " +usr_password)
    else:
        print("invalid user name")
        User_options()
    f.close()

#login method for user login upon successfull completion of the registration
def Login_Exiting_user():
    print("Welcome to login section please provide")
    name = str(input("Name: "))
    password = str(input("Password: "))
    f = open("registration_details.txt",'r')
    info = f.read()
    info = info.split()
    if name in info:
        index = info.index(name) + 1
        usr_password = info[index]
        if usr_password == password:
            print("Welcome Back, " + name)
        else:
            print("Password entered is wrong")
            User_options()
    else:
        print("Name not found. Please Sign Up.or get the forget password")
        print(User_options())

#user function to choose either for regustration or login
def User_options():
    choice = int(input("Enter 1 For registration, Enter 2 for Login and Enter 3 for forget password 0 t0 exit"))
    if choice == 1:
        return User_Registration()
    elif choice == 2:
        return Login_Exiting_user()
    elif choice == 3:
        Forget_password()
    else:
        return

#calling the method in order to perform the user requested operatins
User_options()
