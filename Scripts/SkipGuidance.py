import time
import pyautogui as gui


time.sleep(3)

if(gui.onScreen(1600, 750)):
    gui.click(337, 531, button = "left", clicks = 3, interval = 11)
    print("你在游戏里很安全")
else:
    # Out of the Screen # 保护
    gui.FAILSAFE = False 