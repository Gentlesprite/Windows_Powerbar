# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2024/4/1 14:27
# File:build.py
import os
import shutil

# 最好使用虚拟环境打包

software_name = 'powerbar'
py_name = 'powerbar.py'
icon_path = r'img/powercfg.ico'
upx_dir = r'module/bin/upx.exe'
version_file = os.path.join(os.getcwd(), 'file_version_info.txt')
if __name__ == '__main__':
    try:
        import PyInstaller.__main__

        PyInstaller.__main__.run([
            '--upx-dir', upx_dir,
            '-F',
            '-w',
            '-i', icon_path,
            '--version-file', version_file,
            '--name', software_name,
            py_name
        ])
    except ImportError:
        print('使用pip install pyinstaller安装pyinstaller后重试。')
    finally:
        build_dir = os.path.join(os.getcwd(), 'build')
        if os.path.exists(build_dir):
            shutil.rmtree(build_dir)
