import pyautogui
import time
import subprocess
import pyperclip
import importlib
import easyocr


class Task4:
    def __init__(self):
        self.check_packages()

    def check_packages(self):
        required_packages = ['pyautogui', 'pyperclip', 'easyocr']
        for package in required_packages:
            if not self.check(package):
                print(f"Installing {package}")
                subprocess.check_call(['pip', 'install', package])

    def check(self, package):
        try:
            importlib.import_module(package)
        except ImportError:
            return False
        return True

    def save_notepad_file(self):
        try:
            pyautogui.press('win')
            pyautogui.write('notepad', interval=0.1)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.click()
            pyautogui.write('Query session', interval=0.2)
            output = self.screenshot()
            for word in output:
                if word[1] == 'File':
                    pyautogui.click(word[0][0])
                    time.sleep(2)
                    break
            output_save = self.screenshot()
            for word in output_save:
                if word[1] == 'Save':
                    pyautogui.doubleClick(word[0][0])
                    time.sleep(1)
                    pyautogui.write('sample.bat', interval=0.2)
                    break
            pyautogui.hotkey('ctrl', 'l')
            pyautogui.hotkey('ctrl', 'c')
            file_path = pyperclip.paste().strip()
            path = file_path + '\\sample.bat'
            pyautogui.press('enter')
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.hotkey('alt', 'f4')
            return path
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print('Executed successfully\n')

    def screenshot(self):
        reader = easyocr.Reader(['en'])
        screenshots = pyautogui.screenshot()
        screenshots.save('screenshot.png')
        output = reader.readtext('screenshot.png')
        return output

    def print_output(self):
        path = self.save_notepad_file()
        output = subprocess.run([path], capture_output=True, text=True)
        file1 = open('output.txt', 'w')
        for line in output.stdout.splitlines():
            file1.write(str(line) + '\n')
        print('check output.txt for the output')


if __name__ == "__main__":
    call = Task4()
    call.print_output()
