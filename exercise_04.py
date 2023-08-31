sum = 0
intList = []

for x in range (5):
    while True:
        try:
            intPut = int(input(f'Enter int #{x+1}: '))
            intList.append(intPut)
            break
        except ValueError:
            print('Invalid input. Please enter an int.')
            
for x in intList:
    sum += x
        
print('Your sum is ', sum)
    