# take the input from the user upto which the harmonic value is to be found
num = int(input("Enter the number of which harmonic value is to be found "))
if num!=0:
    sum = 0.0
    for i in range(1,num+1):
        sum = sum + (1/i)
# printing the sum of the value of the nth harmonic numbers
    print(f"Nth harmonic value is = {round(sum,3)}")
else:
    print("the value of n must be greater than 0")