#python在预设的时间自动打开微信给预设的对象发送预设的信息
import pyautogui
import schedule
import subprocess
import time
weChatPath = r"C:\Program Files\Tencent\Weixin\Weixin.exe"
#activate WECHAT
subprocess.Popen(weChatPath)
pyautogui.getWindowsWithTitle('微信')
# winSubj
sizex,sizey=pyautogui.size()
print((sizex,sizey))
posix,posiy=pyautogui.position()
print(posix,posiy)
print(pyautogui.onScreen(posix,posiy))