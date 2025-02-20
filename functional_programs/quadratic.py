import math 
# function to claculate the delta value
def quadratic(a,b,c):
    value = (b**2)-(4*a*c)
    return value
a,b,c = map(int,input("Enter the value of a,b,c each seperated by comma:-").split(','))
delta = quadratic(a,b,c)
# calculating the roots of the equation
root1 = (-b+math.sqrt(delta))/(2*a)
root2 = (-b-math.sqrt(delta))/(2*a)
print(f"the roots of quadratic equation are :- {round(root1,2)} and {round(root2,2)}")

