import tkinter as tk

# создание главного окна
root = tk.Tk()
root.title("Флажки")

# создание текстового поля для вывода результата
result_field = tk.Text(root, width=40, height=10)
result_field.pack()

# создание флажков
checkboxes = [
    ("Числа", ["7", "4", "4", "10", "15"], ["В", "З", "О", "Ф", "Ы", "Г", "И", "П", "Х", "Э"]),
    ("Буквы кириллицы", ["А", "Ё", "М", "Т", "Ш"], ["А", "Ё", "М", "Т", "Ш", "Б", "Ж", "Н", "У", "Щ"]),
    ("Буквы латиницы", ["Д", "К", "Р", "Ц", "Ю"], ["Д", "К", "Р", "Ц", "Ю", "Е", "Л", "С", "Ч", "Я"])
]


def calculate():
    selected_items = []
    for i, (name, items, initials) in enumerate(checkboxes):
        for j, item in enumerate(items):
            if checkboxes_vars[i][j].get() and initials[j] in allowed_initials:
                selected_items.append(item)

    if selected_items:
        if name == "Числа":
            result = sum(map(int, selected_items))
        else:
            result = "".join(selected_items)
        result_field.delete(1.0, tk.END)
        result_field.insert(tk.END, result)
    else:
        result_field.delete(1.0, tk.END)
        result_field.insert(tk.END, "Ничего не выбрано!")


checkboxes_vars = []
allowed_initials = set()

for name, items, initials in checkboxes:
    label = tk.Label(root, text=name)
    label.pack()

    checkbox_vars = []
    for item in items:
        checkbox_var = tk.BooleanVar(value=False)
        checkbox_vars.append(checkbox_var)
        checkbox = tk.Checkbutton(root, text=item, variable=checkbox_var)
        checkbox.pack(anchor=tk.W)

    checkboxes_vars.append(checkbox_vars)
    allowed_initials.update(initials)

# создание кнопки для расчета результата
button_calculate = tk.Button(root, text="Рассчитать", command=calculate)
button_calculate.pack()

# запуск главного цикла
root.mainloop()
