import time
import pyautogui as gui


time.sleep(3)
# 点击应用后，识别是否进入登录界面



if(gui.onScreen(1919, 0)):
    # 回答三个问题

    gui.click(337, 531, button = "left", clicks = 3, interval = 11)
    
    # 需要加敏感字识别判断 重新选名
    gui.moveTo(821, 666, duration = 5)
    gui.click()

    time.sleep(7)
    # 第一场战斗
    gui.click(821, 666, button = 'left', clicks = 4, interval = 1)
    gui.moveTo(165, 102, duration = 2)
    gui.dragTo(240, 473, 1.5, button = 'left')
    time.sleep(8)
    # 放英雄坛
    gui.click(270, 104)
    gui.moveTo(287, 494, duration = 1)
    gui.click()
    
    # 伐竹厂
    gui.moveTo(476, 108, duration = 2)
    gui.dragTo(186, 98, 1)
    time.sleep(2)
    gui.moveTo(463, 96, duration = 1)
    gui.click()
    gui.moveTo(369, 209, duration = 0.5)
    gui.click()

    # 出英雄
    gui.moveTo(278, 472, duration = 6)
    gui.click()
    gui.moveTo(1327, 596, duration = 2)
    gui.click()
    time.sleep(11)
    # 放技能
    gui.click(1144, 94)
    # 玄机营
    gui.moveTo(357, 105, duration=3)
    gui.dragTo(231, 338, button="left")
    time.sleep(8)
    gui.moveTo(252, 280)
    gui.click()
    time.sleep(0.5)
    gui.click(1061, 599)
    # 摘叶飞花
    gui.moveTo(505, 678, duration = 5)
    gui.dragTo(810, 475, button="left", duration=1)
    # 兵营
    time.sleep(1)
    gui.click(250, 100)
    time.sleep(0.5)
    gui.click(55, 98)
    time.sleep(0.5)
    gui.click(372, 474)
    time.sleep(6)
    # 选中兵营
    gui.click(370, 476)
    gui.moveTo(1203, 601, duration = 5)
    gui.click(interval = 5, clicks = 4)



    print("你在游戏里很安全")
else:
    # Out of the Screen # 保护
    gui.FAILSAFE = False 