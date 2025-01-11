import tkinter as tk
import pyautogui as gui
import datetime

# 创建主窗口
root = tk.Tk()
root.title("查看坐标")
root.geometry("200x140")

# label
label = tk.Label(root, text="(X, y)", font=("楷体 常规", 24))
label.pack(pady = 15)
timeStr = tk.StringVar()
timeLabel = tk.Label(root, fg='blue', font=("楷体 常规", 24), textvariable = timeStr)
timeLabel.pack(pady = 15)

# 更新鼠标位置
def update_position():
    x, y = gui.position()
    label.config(text = f'{x}, {y}')
    root.after(50, update_position)
    

def show_time():
    """时 分 秒"""
    now = datetime.datetime.now()
    strTime = now.strftime('%H:%M:%S %p')
    timeStr.set(strTime)
    timeLabel.after(500, show_time)


update_position()
show_time()
root.mainloop()
# 学一下pyinstaller 打包
