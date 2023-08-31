# Chris Li

def countLetter(userInput):
    userInput = userInput.replace(" ", "")
    userInput = userInput.lower()
    countLetter = {}
    for char in userInput:
        if char in countLetter:
            countLetter[char] += 1
        else:
            countLetter[char] = 1
    return countLetter

userInput = input('Please enter a string: ')
output = countLetter(userInput)
print('String letter count: ')
for letter, count in output.items():
    print(f"{letter}: {count}")


