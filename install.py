#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import os

fst = input("你想安装OALJ(OIer && ACMer's Local Judge)吗? (y/n， 默认为y)")
if fst != 'n':
    os.system('cp oalj.py /usr/bin/oalj')
    os.system('cp cogs.py /usr/bin/cogs')
    os.system('cp loj.py /usr/bin/loj')
    ask = input("是否安装pip以及库文件?(y/n, 默认为y)")
    if ask != 'n':
        os.system("sudo apt-get install python3-pip")
        os.system("pip3 install urllib3[socks]")
        os.system("pip3 install colorama")
        os.system("pip3 install request")
else:
    sec = input("你想卸载OALJ(OIer && ACMer's Local Judge)吗? (y/n, 默认为n)")
    if sec != 'n':
        os.system("rm /use/bin/oalj")
        os.system('rm /usr/bin/cogs')
        os.system('rm /usr/bin/loj')
