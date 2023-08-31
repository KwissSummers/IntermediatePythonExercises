def commonDicts(dict1, dict2):
    dictSum = {}
    for var in dict1:
        if var in dict2:
            dictSum[var] = dict1[var] + dict2[var]
    return dictSum

my_dict_1 = {'a': 5, 'b' : 12, 'c': 3, 'd' :9}
my_dict_2 = {'b': 4, 'c' : 9, 'd': 10, 'e': 16}
combined_dict = commonDicts(my_dict_1, my_dict_2)
print(combined_dict)