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
    print('-' * 30)
    if os.system('g++ ./{0} -o temp/main {1} >> temp/compile_log'.format(file, compile_parameter)):
        print('编译错误!!')
        print('-' * 30)
        return 1
    else:
        print("编译成功")
        print('-' * 30)
        return 0

def judge():
    num = 0
    wa = False
    print("序号    结果      时间")
    for j in jing:
        num = num + 1
        infile = j.join(input_name)
        outfile = j.join(output_name)
        begin_time = time.time()
        os.system("temp/main < date/{0} > temp/temp.ans".format(infile))
        if os.system("diff {0} temp/temp.ans date/{1} >> temp/diff_log".format(diff_parameter, outfile)):
            print(" {0}       WA       {1:.0f}ms".format(num, float(time.time() - begin_time) * 1000))
            if wa == False:
                wa = True
                os.system("cp temp/diff_log temp/first_diff_log")
                os.system("cp temp/temp.ans temp/w_a")
                os.system("cp date/{0} temp/f_i_f".format(infile))
                os.system("cp date/{0} temp/f_o_f".format(outfile))
                first = num
        else:
            print(" {0}       AC       {1:.0f}ms".format(num, float(time.time() - begin_time) * 1000))
    if wa:
        print('-' * 30)
        print("你在第{0}个测试点出现了错误,下面是该点的输入数据:".format(first))
        os.system("cat temp/w_a")
        print('-' * 30)
        print("上面带减号\"-\"的是你的输出,下面带加号\"+\"的是答案输出，\"@@\"之间的数字表示行号:")
        with open("temp/first_diff_log") as dl:
            for line in dl:
                print(line, end='')
        print('-' * 30)


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
        print('-' * 30)
        os.system('cat temp/compile_log')
        print('-' * 30)
    else :
        judge()
    os.system("rm -rf temp")
    quit()