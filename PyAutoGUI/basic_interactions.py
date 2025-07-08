import pyautogui
import time
import platform # To detect OS

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5 # Pause for 0.5 seconds after each action

def open_and_type_text(app_name, text_to_type):
    print(f"Attempting to open {app_name}...")
    if platform.system() == "Windows":
        pyautogui.press('win') # Open Start menu
        pyautogui.write(app_name)
        pyautogui.press('enter')
    elif platform.system() == "Darwin": # macOS
        pyautogui.hotkey('command', 'space') # Open Spotlight Search
        pyautogui.write(app_name)
        pyautogui.press('enter')
        # Open a new document
        pyautogui.hotkey('command', 'n')
    else:
        print("This script is for Windows or macOS.")
        return

    time.sleep(2) # Give the application time to open

    print(f"Typing text into {app_name}...")
    pyautogui.write(text_to_type, interval=0.05) # Type characters with a slight delay

    time.sleep(1) # Wait a moment


    # Close the application (without saving)
    print(f"Closing {app_name}...")
    if platform.system() == "Windows":
        pyautogui.hotkey('alt', 'f4') # Close active window
        time.sleep(0.5)
        # Handle "Do you want to save?" dialog if it appears
        # Look for a "Don't Save" or "No" button
        try:
            # You might need to capture a screenshot of your specific "Don't Save" button
            # For simplicity, we'll just press 'n' assuming it's the shortcut for 'No'
            pyautogui.press('n')
        except Exception:
            print("No save dialog detected or dismissed.")
    elif platform.system() == "Darwin": # macOS
        pyautogui.hotkey('command', 'option', 'q') # Quit application
        time.sleep(0.5)
        # Handle "Do you want to save?" dialog if it appears
        try:
            # Look for a "Don't Save" or "Delete" button
            # pyautogui.click('dont_save_button_mac.png') # If you have a screenshot
            pyautogui.press('delete') # Often 'Delete' is the default for "Don't Save"
        except Exception:
            print("No save dialog detected or dismissed.")

    print(f"{app_name} automation complete.")

# Run the automation
if platform.system() == "Windows":
    open_and_type_text("notepad", "This is a test message from PyAutoGUI on Windows.")
elif platform.system() == "Darwin":
    open_and_type_text("textedit", "This is a test message from PyAutoGUI on macOS.")
else:
    print("OS not supported for this specific example.")
