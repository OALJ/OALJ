#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import os

fst = input("你想安装OALJ(OIer && ACMer's Local Judge)吗? (y/n)")
if fst == 'y':
    os.system('cp oalj.py /usr/bin/oalj')
    os.system('g++ oalj_color.cpp -o /usr/bin/oalj_color -g')
else:
    sec = input("你想卸载OALJ(OIer && ACMer's Local Judge)吗? (y/n)")
    if sec == 'y':
        os.system("rm /use/bin/oalj")
        os.system('rm /usr/bin/oalj_color')
