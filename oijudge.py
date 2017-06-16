#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
import sys
import time

def compile(file, parameter):
    if os.system('g++ ./%s -o main %s 2> compile_log' %(file, parameter)):
        print('Compile Error\n')
        print('/////////////////////////////\n')
        os.system('cat ./compile_log')
        os.system('rm ./compile_log')
        print('\n/////////////////////////////')
        quit()
    else: os.system('rm ./compile_log')
l = len(sys.argv)
cpop = '-g -DLOACL'

if l == 1:
    print('-cr [str]         compile and run the [str]')
    print('-cr [str1] [str2] to compile and run [str1] input from [str2]')
    print('-j  [str]         to judge your [str] ****not yet****')
elif l == 3 or l == 4:
    a = sys.argv[1]
    b = sys.argv[2]
    if l == 4:
        c = sys.argv[3]
    compile(b, cpop)
    print('Compile Complete\n')
    if l == 4:
        os.system('./main <%s' %c)
    else: os.system('./main')
    os.system('rm ./main')
quit()