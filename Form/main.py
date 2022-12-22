import tkinter as tk
import threading
import scraper

# Add the TableScraper class from scraper.py
from scraper import TableScraper

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
        if command == "scrape":
            # Create an instance of the TableScraper class
            scraper = TableScraper()

            # Start the scraper in a separate thread
            scraper_thread = threading.Thread(target=scraper.run)
            scraper_thread.daemon = True
            scraper_thread.start()
            self.console.write("Table scraper started\n")
        elif command == "stop":
            # Add code here to stop the scraper
            self.console.write("Table scraper stopped\n")
        elif command == "exit":
            # Add code here to exit the program
            self.console.write("Exiting program\n")
            self.master.destroy()
        else:
            self.console.write("Invalid command\n")

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.console = Console(self)
        self.input_field = InputField(self, self.console)
        self.console.pack(side="top", fill="both", expand=True)
        self.input_field.pack(side="bottom", fill="x")
        # Add a welcome message to the console
        self.console.write("Welcome to the table scraper console!\n")
        self.console.write("Type 'scrape' to start the scraper, 'stop' to stop the scraper, or 'exit' to exit the program.\n")

def run_console():
    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    run_console()
