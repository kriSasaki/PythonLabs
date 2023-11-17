
def contains_123_combination(lst):
    # Преобразуем список в строку, чтобы легче искать комбинации
    string_list = ''.join(map(str, lst))
    
    # Проверяем наличие комбинаций 1, 2, 3
    if '123' in string_list or '132' in string_list or '213' in string_list or '231' in string_list or '312' in string_list or '321' in string_list:
        return True
    else:
        return False

# Пример использования
my_list = [4, 1, 2, 3, 5, 6]
result = contains_123_combination(my_list)
print(result)  # Выведет True, так как список содержит комбинацию 1, 2, 3
