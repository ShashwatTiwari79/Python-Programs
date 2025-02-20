# take the user input in UserName variable
UserName = input("Enter username ")
# check if the length of user input is greater than or equal to 3 
if len(UserName)>=3:
    print(f"Hello {UserName}, How are you?")
else:
    print("Ensure that the length of user is atleast minimum of 3 characters")