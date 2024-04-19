import pyautogui#需要在终端pip install pyautogui，可能需要重启一下编辑器
import time as T
with open('test.txt', 'r',encoding='utf-8') as file: #不指定路径的话默认的是与此脚本同文件夹
    content = file.read() 
    print(content)
#words = list(content)
def TYPE():
    for word in content:
        print(word)
        T.sleep(0.1)
        pyautogui.typewrite(word)
interval=6

while interval>0:
    interval -= 1
    print(f"将在{interval}秒后开始执行，请确保就绪",end="\r")#\r是覆写
    T.sleep(1)
TYPE()
