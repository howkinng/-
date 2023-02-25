import tkinter as tk

def continue_message():
    message = "Продолжение сообщения..."
    text_field.insert(tk.END, message)

# создание главного окна
root = tk.Tk()
root.title("Пример окна")

# создание текстового поля
text_field = tk.Text(root, width=40, height=10)
text_field.pack()

# создание поля ввода пароля
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# создание кнопки для продолжения вывода сообщения
button_continue = tk.Button(root, text="Продолжить", command=continue_message)
button_continue.pack()

# запуск главного цикла
root.mainloop()

