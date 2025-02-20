# defined a function to check whether its a leap year or not
def leap_year(num: int):
    if num%4==0:
        if num%100==0:
            return num%400==0
        return True
    else:
        return False 
# user input to take the year as input
year = input("Enter the year to check whether its a leap year or not ")
# check whether length of the input given by the user is 4 or not
if len(year)==4:
    check = leap_year(int(year))
# check whether its a leap year or not
    if check==True:
        print("Its a leap year")
    else:
        print("Its not a leap year")
else:
    print("length of year should be of 4 digits")