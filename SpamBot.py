import pyautogui
import time

def mesaj():
    pyautogui.press('enter')

kullanicimesaj = input("Spamlamak İstediğiniz Mesaj:")

time.sleep(5)
while True:
    pyautogui.write(kullanicimesaj)
    mesaj()
    time.sleep(0.1)