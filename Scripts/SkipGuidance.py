import time
import pyautogui as gui


time.sleep(3)

if(gui.onScreen(1600, 750)):
    # 回答三个问题
    #gui.click(337, 531, button = "left", clicks = 3, interval = 11)

    gui.moveTo(821, 666,duration=0.5)
    gui.click()

    print("你在游戏里很安全")
else:
    # Out of the Screen # 保护
    gui.FAILSAFE = False 