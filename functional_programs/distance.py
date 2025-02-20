import math 
# function for calculating the euclidean distance
def euclidean(x,y):
    distance = math.sqrt(x**2+y**2)
    return distance
x,y = map(int,input("Enter values of x and y seperated by comma:-").split(','))
dist = euclidean(x,y)
print(f"Euclidean distance is equal to :- {round(dist,2)}")


