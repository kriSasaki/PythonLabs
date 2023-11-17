def generate_elements_in_range(input_list, a, b):
    if a >= len(input_list) or b >= len(input_list):
        raise ValueError("The values of a and/or b are greater than the length of the list")
    
    for i in range(a, b + 1):
        yield input_list[i]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = 2
b = 7

try:
    for element in generate_elements_in_range(my_list, a, b):
        print(element)
except ValueError as e:
    print(e)
