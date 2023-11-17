import sqlite3

def find_record(table_name, field_name, field_value):
    # ������������ � ���� ������ (�������� "example.db" �� ��� ����� ���� ������)
    connection = sqlite3.connect("example.db")
    cursor = connection.cursor()

    # ��������� SQL-������ � �������������� ���������� ��� �������������� SQL-��������
    query = f"SELECT id FROM {table_name} WHERE {field_name} = ?"
    cursor.execute(query, (field_value,))

    # �������� ��������� �������
    result = cursor.fetchone()

    # ��������� ���������� � ����� ������
    connection.close()

    # ���������� ��������� (������������� ������ ��� None, ���� ������ �� �������)
    return result[0] if result else None

# ������ �������������
table_name = "your_table"
field_name = "your_field"
field_value = "desired_value"

record_id = find_record(table_name, field_name, field_value)

if record_id is not None:
    print(f"������ �������! ������������� ������: {record_id}")
else:
    print("������ �� �������.")

