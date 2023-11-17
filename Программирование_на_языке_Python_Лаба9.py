import tkinter as tk
from tkinter import ttk
import sqlite3

class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database GUI App")

        self.db_connection = None
        self.query_result_var = tk.StringVar()

        self.label_db_name = tk.Label(root, text="Имя БД:")
        self.entry_db_name = tk.Entry(root)
        self.button_connect = tk.Button(root, text="Подключиться", command=self.connect_to_db)

        self.label_query = tk.Label(root, text="Запрос:")
        self.entry_query = tk.Entry(root)
        self.button_execute = tk.Button(root, text="Выполнить", command=self.execute_query)

        self.label_result = tk.Label(root, text="Результат:")
        self.result_text = tk.Text(root, height=10, width=50, state=tk.DISABLED)

        self.label_db_name.grid(row=0, column=0, padx=10, pady=10)
        self.entry_db_name.grid(row=0, column=1, padx=10, pady=10)
        self.button_connect.grid(row=0, column=2, padx=10, pady=10)

        self.label_query.grid(row=1, column=0, padx=10, pady=10)
        self.entry_query.grid(row=1, column=1, padx=10, pady=10)
        self.button_execute.grid(row=1, column=2, padx=10, pady=10)

        self.label_result.grid(row=2, column=0, padx=10, pady=10)
        self.result_text.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

    def connect_to_db(self):
        db_name = self.entry_db_name.get()
        try:
            self.db_connection = sqlite3.connect(db_name)
            self.show_result("Подключение к БД успешно.")
        except sqlite3.Error as e:
            self.show_result(f"Ошибка подключения к БД: {e}")

    def execute_query(self):
        if not self.db_connection:
            self.show_result("Сначала подключитесь к БД.")
            return

        query = self.entry_query.get()
        try:
            cursor = self.db_connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            self.show_result(result)
        except sqlite3.Error as e:
            self.show_result(f"Ошибка выполнения запроса: {e}")

    def show_result(self, result):
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, str(result))
        self.result_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()

