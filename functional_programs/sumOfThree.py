# function to claculate the tripelts
def triplets(arr):
    res = []
    size = len(arr)

    for i in range(0,size-2):
        for j in range(i+1,size-1):
            for k in range(j+1,size):
                if arr[i]+arr[j]+arr[k]==0:
                    res.append([i,j,k])
    return res
num = int(input("Enter size of the array:-"))
# taking input into the array
print("Enter values into the array:-")
array = []
for i in range(0,num):
    array.append(int(input()))
result = triplets(array)

print("The triplets are:-")
for values in result:
    print(values[0],values[1],values[2])

