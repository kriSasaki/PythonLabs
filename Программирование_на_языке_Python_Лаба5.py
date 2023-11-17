def count_russian_chars(file_path):
    result_dict = {}

    russian_alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
            for char in content:
                if char.lower() in russian_alphabet:
                    result_dict[char] = result_dict.get(char, 0) + 1

    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    return result_dict

file_path = "C:\Games\SHEESH.txt"
result = count_russian_chars(file_path)
print(result)
