import importlib
import subprocess
import time
import qrcode
from PIL import Image
import cv2
from pyzbar.pyzbar import decode


class QR_handling():

    def __init__(self):
        self.check_packages()

    def check_packages(self):

        required_packages = ['qrcode', 'PIL', 'cv2', 'pyzbar']
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

    def text_to_qr(self, text):
        qr_code = qrcode.make(text)
        qr_code.save("qrcode.png")
        img = Image.open('qrcode.png')
        img.show()

    def qr_to_text(self, path):
        start_time = time.time()
        image = cv2.imread(path)
        if image is None:
            print(f"Error: Unable to load image from {path}")
            return
        qr = decode(image)
        for data in qr:
            qr_bytes = data.data
            qr_str = qr_bytes.decode('utf-8')
        file2 = open('output.txt', 'w')
        file2.write(str(qr_str) + '\n')
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time:{execution_time}")

    def run(self):
        n = int(input('Do you want to encode or decode?\n1-Encode\n0-Decode\n2-Both\n'))
        if n == 1:
            text_to_encode = input('Type the string to be converted to a QR Code:')
            file1 = open('input.txt', 'w')
            file1.write(str(text_to_encode) + '\n')
            self.text_to_qr(text_to_encode)
        elif n == 0:
            qr_path = input('Enter the path of the file:')
            self.qr_to_text(qr_path)
        elif n == 2:
            text_to_encode = input('Type the string to be converted to a QR Code:')
            file1 = open('input.txt', 'w')
            file1.write(str(text_to_encode) + '\n')
            self.text_to_qr(text_to_encode)
            qr_path = input('Enter the path of the file:')
            self.qr_to_text(qr_path)
        else:
            print('Invalid Input')


call = QR_handling()
call.run()
