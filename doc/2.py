# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2024/3/27 17:39
# File:2
from PySide2.QtCore import QFile, QFileInfo
import os


def createShortcut():

    lnkName = "Umi-OCR"
    appPath = r'D:\files\Documents\study\python\Program\windows_power_manager\powerbar2.exe'
    # if not appPath:
    #     return "未找到 Umi-OCR.exe 。请尝试手动创建快捷方式。\n[Error] Umi-OCR.exe APP_PATH not exist. Please try creating a shortcut manually."
    lnkPathBase = os.getenv("ProgramData") + "\\Microsoft\\Windows\\Start Menu" + "\\Programs\\Startup"
    print(lnkPathBase)
    lnkPathBase = os.path.join(lnkPathBase, lnkName)
    lnkPath = lnkPathBase + ".lnk"
    i = 1
    while os.path.exists(lnkPath):  # 快捷方式已存在
        lnkPath = lnkPathBase + f" ({i}).lnk"  # 添加序号
        i += 1
    appFile = QFile(appPath)
    res = appFile.link(lnkPath)
    if not res:
        return f"[Error] {appFile.errorString()}\n请尝试以管理员权限启动软件。\nPlease try starting the software as an administrator.\nappPath: {appPath}\nlnkPath: {lnkPath}"
    return "[Success]"


def deleteShortcut():  # 删除快捷方式
    appName = "Umi-OCR"
    lnkDir = os.getenv("ProgramData") + "\\Microsoft\\Windows\\Start Menu" + "\\Programs\\Startup"
    num = 0
    for fileName in os.listdir(lnkDir):
        lnkPath = os.path.join(lnkDir, fileName)
        try:
            if not os.path.isfile(lnkPath):  # 排除非文件
                continue
            info = QFileInfo(lnkPath)
            if not info.isSymLink():  # 排除非快捷方式
                continue
            originName = os.path.basename(info.symLinkTarget())
            if appName in originName:  # 快捷方式指向的文件名包含appName，删之
                os.remove(lnkPath)
                num += 1
        except Exception as e:
            print(f"[Error] 删除快捷方式失败 {lnkPath}: {e}")
            continue
    return num
createShortcut()