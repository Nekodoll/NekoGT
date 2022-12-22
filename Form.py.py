import tkinter as tk
import threading
import scraper


class Console(tk.Text):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.config(state="disabled")

    def write(self, text):
        self.config(state="normal")
        self.insert("end", text)
        self.see("end")
        self.config(state="disabled")


class InputField(tk.Entry):
    def __init__(self, parent=None, console=None):
        super().__init__(parent)
        self.console = console
        self.bind("<Return>", self.on_enter)

    def on_enter(self, event):
        command = self.get()
        self.delete(0, "end")
        self.console.write(f"Running command: {command}\n")
        # Add code here to run the command and print the output to the console


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.console = Console(self)
        self.input_field = InputField(self, self.console)
        self.console.pack(side="top", fill="both", expand=True)
        self.input_field.pack(side="bottom", fill="x")


def run_console():
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    run_console()
