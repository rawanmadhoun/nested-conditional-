user_name = input(" enter your user name")
pass_word = int(input(" enter your Pass word"))
user_role = input ("user role ")
# the program ask for user name 
user_name = "Ahmed"
pass_word = "123456" 
user_role = "Admin"
user_role = "moderator" 
user_role = "user"
if user_name == "Ahmed":
    print (" please enter the password ")
    if pass_word == "123456" :
        print ("please add your role")
        if user_name == "Admin":
            print ("welcome Admin") 
        elif user_role == "moderator": 
            print ("Welcome moderator")
        elif user_role == "user":
            print ("welcome user")
        else:
            print ("unkonwn user")

    else:
        Print ("Wrong Password") 
else :
    print ("user not found")






