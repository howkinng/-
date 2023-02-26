import tkinter as tk
from tkinter import ttk
import time
import wikipedia


# class of Parser app
class ParserApp:
    # creating window
    root = tk.Tk()
    root.title("Text")

    def __init__(self, command=None):
        # setting size
        width = 600
        height = 500
        self.root.geometry(f'{width}x{height}+450+200')
        self.command = command
        # creating elements in window
        header = tk.Label(self.root, text="Wikipedia", font=("Arial", 20, "bold"), borderwidth=1, relief="solid")
        input_label = tk.Label(self.root, text="Input query text:", font=("Arial", 14), borderwidth=1, relief="solid")
        self.string_entry = tk.StringVar()
        self.search_request = None
        self.query_entry = tk.Entry(self.root, borderwidth=1, relief="solid", textvariable=self.string_entry)
        accept_button = tk.Button(self.root, text="Search", command=self.command, borderwidth=1, relief="solid")
        self.waiting = tk.Label(self.root, text="Please, wait ...", font=("Arial", 14), borderwidth=1, relief="solid")
        self.output = tk.Frame(self.root, borderwidth=1, relief="solid")
        self.answer = tk.Text(self.output, height=4, wrap="word", state="disabled", width=30)
        self.result_label = None

        # packing elements
        header.grid(row=0, column=0, columnspan=2, stick="we")
        input_label.grid(row=1, column=0, stick="e")
        self.query_entry.grid(row=1, column=1, stick="w")
        accept_button.grid(row=2, column=0, columnspan=2)
        self.waiting.grid(row=3, column=0, columnspan=2, sticky="we")
        self.waiting.grid_remove()
        # setting minimum size for each column
        self.root.grid_columnconfigure(0, minsize=300)
        self.root.grid_columnconfigure(1, minsize=300)
        self.output.grid_columnconfigure(0, minsize=577)
        self.output.grid_columnconfigure(1, minsize=23)

    # method that shows root window
    def show(self):
        self.root.mainloop()

    def show_results(self, results):
        self.answer.config(height=int(len(results) / 3))
        if not len(self.answer.get("1.0", 'end-1c')):
            self.answer.grid(row=0, column=0, stick="we")
            y_scroll = ttk.Scrollbar(self.output, orient='vertical', command=self.answer.yview)
            self.answer['yscrollcommand'] = y_scroll.set
            y_scroll.grid(row=0, column=1, stick='ns')
        self.answer.config(state="normal")
        self.answer.delete("1.0", tk.END)
        self.answer.insert("1.0", results)
        self.answer.config(state="disabled")
        self.output.grid(row=4, column=0, columnspan=2, sticky="wens")

    def create_waiting(self):
        print("create")
        self.waiting.grid()

    def destroy_waiting(self):
        self.waiting.destroy()
        print("destroy")


def test():
    app.create_waiting()
    app.root.update()
    time.sleep(2)
    app.destroy_waiting()
    print(app.query_entry.get())
    wikipedia.set_lang("ru")
    text = wikipedia.summary(app.query_entry.get(), sentences=2)
    app.show_results(text)


# main code block
def main():
    app.show()


# entry point
if __name__ == "__main__":
    app = ParserApp(test)
    main()
