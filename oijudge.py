#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
import sys
import time

# 编译选项
compile_parameter = "-DLOCAL -O2 -g -Wall"
# diff选项
diff_parameter = "-U 0 -b -B -w"

def compile(file):
    if os.system('g++ ./{0} -o temp/main {1} >> temp/compile_log'.format(file, compile_parameter)):
        print('Compile Error\n')

        return 1
    else:
        print("Copile Accept\n")
        return 0

def judge():
    num = 0
    wa = False
    for j in jing:
        num = num + 1
        infile = j.join(input_name)
        outfile = j.join(output_name)
        os.system("temp/main < date/{0} > temp/temp.ans".format(infile))
        if os.system("diff {0} temp/temp.ans date/{1} >> temp/diff_log".format(diff_parameter, outfile)):
            print("{0} WA".format(num))
            if wa == False:
                wa = True
                os.system("cp temp/diff_log temp/first_diff_log")
                first = num
        else:
            print("{0} AC".format(num))
    print()
    if wa:
        print("WA on {0}\n".format(first))
        print('/' * 55 + '\n')
        with open("temp/first_diff_log") as dl:
            for line in dl:
                print(line, end='')
        print('\n' + '/' * 55)

if __name__ == '__main__':
    with open("./config.txt", "r+") as config:
        lst = list([])
        for line in config:
            temp = line.split(':')[1].strip()  # 去除两边空格
            lst.append(temp)
    file = lst[0]
    input_name = lst[1].split('#')
    output_name = lst[2].split("#")
    jing = lst[3].split(' ')
    os.system("rm -rf temp")
    os.system("mkdir temp")
    if compile(file):
        print('/' * 55 + '\n')
        os.system('cat temp/compile_log')
        print('\n' + '/' * 55)
    else :
        judge()
    os.system("rm -rf temp")
    quit()