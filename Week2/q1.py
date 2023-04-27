print("This program is to implement a simple calculator.")

a = int(input("Please enter the 1st number: "))
b = int(input("Please enter the 2nd number: "))
operation = input("Please enter the operation: ")
result = 0

if(operation == '+'):
    result = a + b
elif(operation == '-'):
    result = a - b
elif(operation == "*"):
    result = a * b
else:
    if(b == 0):
        result = "Error for the 2nd number!"
    else:
        result = a / b

print(result)