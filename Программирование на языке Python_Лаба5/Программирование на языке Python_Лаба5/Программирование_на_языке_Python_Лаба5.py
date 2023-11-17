

def count_russian_chars(file_path):
    result_dict = {}

    # Генерация символов русского алфавита с помощью ord() и chr()
    russian_alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
            # Подсчет количества каждого символа русского алфавита в файле
            for char in content:
                if char.lower() in russian_alphabet:
                    result_dict[char] = result_dict.get(char, 0) + 1

    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    return result_dict

# Пример использования
file_path = "C:\Games\SHEESH.txt"  # Замените на реальный путь к вашему файлу
result = count_russian_chars(file_path)
print(result)
