import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog, messagebox, scrolledtext, Toplevel
from pygments import highlight
from pygments.lexers import get_lexer_for_filename
from pygments.formatters import HtmlFormatter
from tkinter import font
from tkinter import Text
from io import StringIO
from webbrowser import open_new
import csv
import os
from datetime import datetime
import subprocess


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the window title and background color
        self.title("XS Script and .bat File Checker")
        self.configure(bg='black')

        # Make the window resizable
        self.resizable(True, True)

        # Unsafe commands list
        self.unsafe_commands = ['rm ', 'del ', 'format ', 'rmdir ', ':(){ :|: & };:']

        # Supported file types
        self.file_types = [
            ('Batch Files', '*.bat'),
            ('Shell Scripts', '*.sh'),
            ('Python Scripts', '*.py'),
            ('JavaScript Files', '*.js'),
            ('All Files', '*.*')
        ]

        # Path for the report CSV file
        self.csv_file_path = "reports.csv"

        # Initialize the CSV file with headers if it doesn't exist
        if not os.path.exists(self.csv_file_path):
            with open(self.csv_file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Script Name", "Report"])

        self.initialize_ui()

    def initialize_ui(self):
        # Label for 'by SamuraiSyntax' text
        self.by_label = tk.Label(self, text="BY SamuraiSyntax", bg="black", fg="white", font=("Arial", 12, "bold"))
        self.by_label.pack(anchor='e', padx=10, pady=5)

        # Frame for Text and line number Labelframe
        self.line_text_frame = tk.Frame(self, bg='black')
        self.line_text_frame.pack(fill='both', expand=True)

        # Text field to input script
        self.script_field = scrolledtext.ScrolledText(self.line_text_frame, height=20, bg="grey", fg="white")
        self.script_field.pack(side='right', fill='both', expand=True)

        # Line number field
        self.line_number_field = Text(self.line_text_frame, width=4, padx=3, takefocus=0, border=0, background='grey',
                                      state='disabled', wrap='none')
        self.line_number_field.pack(side='left', fill='y')

        # Bind events
        self.script_field.bind('<KeyRelease>', self._on_change)
        self.script_field.bind('<Button-1>', self._on_change)

        # Button to check script
        self.check_button = ctk.CTkButton(self, text="Check if script is safe", command=self.check_script)
        self.check_button.pack(pady=10)

        # Button to open script file
        self.open_button = ctk.CTkButton(self, text="Open script file", command=self.open_file)
        self.open_button.pack(pady=10)

        # Python script runner section
        self.runner_label = tk.Label(self, text="Python Script Runner", bg="black", fg="white",
                                     font=("Arial", 12, "bold"))
        self.runner_label.pack(pady=5)

        # Text field to input Python script to run
        self.run_field = scrolledtext.ScrolledText(self, height=20, bg="grey", fg="white")
        self.run_field.pack(fill='both', expand=True)

        # Button to run Python script
        self.run_button = ctk.CTkButton(self, text="Run Python script", command=self.run_python)
        self.run_button.pack(pady=10)

    def _on_change(self, event):
        self.line_number_field.config(state='normal')
        self.line_number_field.delete('1.0', 'end')
        number_of_lines = self.script_field.index('end - 1 line').split('.')[0]
        line_numbers_string = "\n".join(str(no) for no in range(1, int(number_of_lines) + 1))
        self.line_number_field.insert('1.0', line_numbers_string)
        self.line_number_field.config(state='disabled')

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=self.file_types)

        if file_path:
            with open(file_path, 'r') as file:
                self.script_field.delete('1.0', tk.END)
                self.script_field.insert('1.0', file.read())

    def check_script(self):
        script = self.script_field.get('1.0', tk.END)
        report = self.get_safety_report(script)
        html_content = highlight(report, get_lexer_for_filename("report.py"), HtmlFormatter(full=True, style="monokai"))
        now = datetime.now()
        dt_string = now.strftime("%d%m%Y%H%M%S")
        html_file_path = f"report_{dt_string}.html"
        with open(html_file_path, 'w') as html_file:
            html_file.write(html_content)

        # Write the report to the CSV file
        with open(self.csv_file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([f"Report {dt_string}", report])

        messagebox.showinfo("Report Generated",
                            f"Report has been saved as {html_file_path}. Open it in your browser to view.")

    def get_safety_report(self, script):
        report = ""
        for index, line in enumerate(script.split("\n"), start=1):
            if any(unsafe_command in line for unsafe_command in self.unsafe_commands):
                report += f"Line {index}: contains potentially unsafe command\n"

        if not report:
            report = "The script appears to be safe.\n"

        return report

    def run_python(self):
        python_code = self.run_field.get('1.0', tk.END)
        try:
            exec(python_code)
            messagebox.showinfo("Success", "Python script executed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while running the script: {e}")


if __name__ == "__main__":
    app = Application()
    app.mainloop()
