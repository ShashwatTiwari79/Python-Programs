# taking input into the array in rowise format
def input_array(rows,cols):
    matrix = []
    print("Enter in the rowise format :- ")
    for i in range(0,rows):
        arr = []
        arr.append(input())
        matrix.append(arr)
    return matrix
# printing the array
def print_array(matrix,row):
    print("Output of the array is:-")
    for i in range(row):
            print(matrix[i])
# taking input of rows and columns
rows = int(input("Enter number of rows:-"))
cols = int(input("Enter number of columns:-"))
array = input_array(rows,cols)
print_array(array,rows)
