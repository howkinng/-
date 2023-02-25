import tkinter as tk

class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.click_count = 0
        self.number = 2
        self.create_widgets()

    def create_widgets(self):
        self.button = tk.Button(self)
        self.button["text"] = "Нажми на меня"
        self.button["command"] = self.update_label
        self.button.pack(side="top")

        self.label = tk.Label(self, text="")
        self.label.pack()

    def update_label(self):
        self.click_count += 1
        self.label["text"] = f"Щелчок №{self.click_count}: {self.number}"
        self.number += 2 if self.number % 2 == 0 else 1

root = tk.Tk()
app = MainWindow(master=root)
app.mainloop()
