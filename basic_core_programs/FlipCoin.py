import random 
# defined a function to calculate the percentage and return it from where it was called
def calculate_percentage(count,number):
    return count/(float(number))*100
# take the user input in num which will store the number of times coin will be tossed
num = int(input("Enter number of times the coin should be tossed "))

head_count = 0

tail_count = 0
# checking whether the number of times to be tossed is greater than 0 or not
if num>0:
# for loop to calculate the total number of heads ad tails
    for i in range (0,num):
        value = random.random()
        if value>0.5:
            head_count += 1
        else:
            tail_count += 1

heads = calculate_percentage(head_count,num)
tails = calculate_percentage(tail_count,num)
print(f"Percentage of Heads = {heads}%")
print(f"Percentage of tails = {tails}%")