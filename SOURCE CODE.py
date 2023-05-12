import pyautogui as mes
import time
inp = input("Enter the message: ")
times = int(input("How many times do you wanna send the message: "))
time.sleep(3)
for i in range(times):
    mes.typewrite(inp)
    mes.press('Enter')