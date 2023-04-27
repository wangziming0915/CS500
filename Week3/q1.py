decimalNum = int(input("Enter a decimal value (0 to 15): "))
if(decimalNum < 10):
    hexNum = decimalNum
elif(decimalNum == 10):
    hexNum = "A"
elif(decimalNum == 11):
    hexNum = "B"
elif(decimalNum == 12):
    hexNum = "C"
elif(decimalNum == 13):
    hexNum = "D"
elif(decimalNum == 14):
    hexNum = "E"
elif(decimalNum == 15):
    hexNum = "F"

print("The hex value is", hexNum)
