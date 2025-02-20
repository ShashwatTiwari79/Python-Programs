# take the input of number which will be used to calculate the power of two
num = int(input("Enter power upto which the value is to be printed "))
# check if the value of num is in the range or not
if num>=0 and num<31:
    for i in range(1,num):

        print(f"2 ^ {i} = {2**i}")
else:
    print("The value of num should be in range from 0 to 31 only")
