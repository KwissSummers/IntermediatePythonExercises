def onlyUnique(inputList):
    uniqueList = []
    for var in inputList:
        if var not in uniqueList:
            uniqueList.append(var)
    return uniqueList

my_list = [1, 2, 3, 2, 1, 4]
unique_list = onlyUnique(my_list)
print(unique_list)