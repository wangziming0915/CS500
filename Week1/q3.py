print("This program calculates n + 2nn + 3nnn of the value from user.")

n = int(input("Please enter an integer :"))

if not isinstance(n, int):
    print("The input is invalid.")
else:
    str0 = str(n)
    str1 = "2" + str0 + str0
    str2 = "3" + str0 + str0 + str0
    result = n + int(str1) + int(str2)
    print("The result of calculation is :" + str(result))