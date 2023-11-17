def contains_123_combination(lst):
    string_list = ''.join(map(str, lst))
    
    if '123' in string_list or '132' in string_list or '213' in string_list or '231' in string_list or '312' in string_list or '321' in string_list:
        return True
    else:
        return False

my_list = [4, 1, 2, 3, 5, 6]
result = contains_123_combination(my_list)
print(result)
