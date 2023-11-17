import sqlite3

def find_record(table_name, field_name, field_value):
    # Подключаемся к базе данных (замените "example.db" на имя вашей базы данных)
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()

    # Формируем SQL-запрос с использованием параметров для предотвращения SQL-инъекций
    query = f"SELECT id FROM {table_name} WHERE {field_name} = ?"
    cursor.execute(query, (field_value,))

    # Получаем результат запроса
    result = cursor.fetchone()

    # Закрываем соединение с базой данных
    connection.close()

    # Возвращаем результат (идентификатор записи или None, если запись не найдена)
    return result[0] if result else None

# Пример использования
table_name = "your_table"
field_name = "your_field"
field_value = "desired_value"

record_id = find_record(table_name, field_name, field_value)

if record_id is not None:
    print(f"Запись найдена! Идентификатор записи: {record_id}")
else:
    print("Запись не найдена.")

