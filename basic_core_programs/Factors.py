num = int(input("Enter number of which prime factors is to be calculated :- "))
value=2
# while loop to calculate the prime factors
print(f"factors of {num} are:-")
while value * value < num:
     while num % value == 0:
         print(value)
         n = n / value
     value = value + 1
# when the loop terminates the last value which is stored in the n should be printed as it is also a factor of number
if num>1:
     print(int(num))
          