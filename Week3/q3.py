print("This program creates a triangle depends on the width.")

width = int(input("Enter the width: "))
k = 0
arr = []


for space in range(0, width):
    arr.append(" ")

row = width - 1

print(row)
while(row >= 0):
    arr[row] = "*"
    print("".join(arr))
    row -= 1

for space in range(0, width - 1):
    arr[space] = " "
    print("".join(arr))
