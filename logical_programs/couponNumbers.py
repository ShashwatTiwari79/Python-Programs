import random
# to calculate the count of random numbers taken to reach all the distinct numbers
def calculate_coupon(num):
    distinct_numbers = set()
    random_numbers_count = 0
# loop will run untill all the distinct numbers are found upto n
    while len(distinct_numbers)<num:
        number = random.randint(0,num-1)
        distinct_numbers.add(number)
        random_numbers_count += 1
    print(f"The distinct coupons are :- {distinct_numbers}")
    print(f"The total number of random numbers generated were :- {random_numbers_count}")
number = int(input("Enter the value of N:-"))
calculate_coupon(number)

