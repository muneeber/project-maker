import os
import subprocess
import webbrowser

# Prompt the user for the project name
project_name = input("Enter the project name: ")

# Define the project folder path
htdocs_path = "C:/xampp/htdocs"
project_path = os.path.join(htdocs_path, project_name)

# Create the project folder in htdocs
os.makedirs(project_path, exist_ok=True)

# Start XAMPP (You may need to adjust the path to your XAMPP control panel executable)
xampp_path = "C:/xampp/xampp-control.exe"

# Start Apache and MySQL using a single subprocess call
subprocess.Popen([xampp_path, "start", "apache", "mysql"])

# Wait for XAMPP control panel to start (adjust the sleep duration as needed)
import time
time.sleep(5)

# Open the project folder in VSCode (You need to have VSCode installed and added to your PATH)
vscode_path = "C:/Users/Hackeeb/AppData/Local/Programs/Microsoft VS Code/bin/code.cmd"
subprocess.Popen([vscode_path, project_path])

# Open localhost in Chrome
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
localhost_url = f"http://localhost/{project_name}"
phpmyadmin_url = "http://localhost/phpmyadmin/"
webbrowser.open(localhost_url, new=2)
webbrowser.open(phpmyadmin_url, new=2)

print("Automation complete!")
