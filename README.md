# SCCHECK
Script checker
# Python Script and .bat File Checker

The XS Script and .bat File Checker is a Python script that allows you to check the safety of scripts and .bat files. It provides a graphical user interface (GUI) where you can paste scripts, check their safety, and generate safety reports.

## Features

- **Script Safety Check**: The application allows you to paste scripts into a text box and check if they contain potentially unsafe commands. It scans the script for specific unsafe commands and generates a safety report.

- **File Safety Check**: In addition to pasting scripts, you can also open .bat files to check their safety. The application scans the contents of the .bat file and provides a safety report.

- **HTML Report Generation**: When a safety check is performed, the application generates an HTML report highlighting any potentially unsafe commands found in the script or .bat file. The report includes line numbers and syntax highlighting for easy analysis.

- **Save Reports**: The generated safety reports are saved as HTML files. Each report has a unique name, making it easier to manage and reference the reports. The reports are also saved in a CSV file, providing a consolidated record of all safety checks performed.

- **Python Script Runner**: The application also includes a section where you can input Python scripts and run them. This feature allows you to execute Python code directly within the application.

## Usage

1. **Check Script Safety**:
   - Paste the script you want to check into the script text box.
   - Click the "Check if script is safe" button to perform the safety check.
   - The application will generate an HTML report highlighting any potentially unsafe commands found in the script. The report will be saved as an HTML file and added to the CSV report file.

2. **Check .bat File Safety**:
   - Click the "Open script file" button to open a .bat file.
   - The contents of the .bat file will be displayed in the script text box.
   - Click the "Check if script is safe" button to perform the safety check.
   - The application will generate an HTML report highlighting any potentially unsafe commands found in the .bat file. The report will be saved as an HTML file and added to the CSV report file.

3. **Run Python Scripts**:
   - Enter the Python script you want to run into the Python script text box.
   - Click the "Run Python script" button to execute the script.
   - The output of the script will be displayed in the console.

## Safety Considerations

- While the XS Script and .bat File Checker helps identify potentially unsafe commands, it is not foolproof. Always review the generated reports and exercise caution when running scripts from untrusted sources.

- Be aware that running arbitrary code can be dangerous. Only run scripts that you trust and understand.

## Requirements

- Python 3.x
- Tkinter library
- CustomTkinter library
- Pygments library

## License

This project is licensed under the [MIT License](LICENSE).

