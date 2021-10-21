#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import os
import platform

fst = input("Do you wanna install OALJ? (y/n，y)")

if fst.lower() != 'n':
    os.system('sudo cp oalj.py /usr/bin/local/oalj')
    ask = input("Wanna install pip, axel? (y/n, y)")
    if ask.lower() != 'n':
        
        os.system("sudo apt-get install python3-pip")
        os.system("sudo apt-get install axel")
        
        os.system("sudo pip3 install urllib3[socks]")
        os.system("sudo pip3 install colorama")
        os.system("sudo pip3 install psutil")
else:
    sec = input("Wanna remove OALJ? (y/n, n)")
    if sec != 'n':
        os.system("sudo rm /use/local/bin/oalj")
