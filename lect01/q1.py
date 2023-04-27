print("Enter a single letter, and I will tell you what the corresponding digit is on the telephone.")

letterMap = {'A':'2','B':'2','C':'2','D':'3','E':'3','F':'3','G':'4','H':'4','I':'4','J':'5','K':'5','L':'5','M':'6','N':'6', 'O':'6','P':'7','R':'7','S':'7','T':'8','U':'8','V':'8','W':'9','X':'9','Y':'9'}

inputLetter = input()

if(not inputLetter.isupper()):
    print("Invalid input!")
elif inputLetter == 'Q' or inputLetter == 'Z':
    outputDigit = 'no'
else:
    print("The digit " + str(letterMap[inputLetter]) + " corresponds to the letter" + inputLetter + " on the telephone.")

