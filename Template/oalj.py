#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
import sys
import time
import colorama 
from colorama import init, Fore
import psutil
# 编译选项
compile_parameter = "-DLOCAL -O2 -Wall"
# diff选项
diff_parameter = "-U 0 -b -B -w"
color_map = { 1:Fore.RED, 2:Fore.GREEN, 3:Fore.YELLOW, 4:Fore.BLUE, 5:Fore.MAGENTA, 6:Fore.CYAN, 7:Fore.WHITE}
def col_print(str, col):
    init(autoreset=True)
    str = str.replace('/', '\n')
    print(color_map[col] + str, end = "")

def print_line():
    col_print('-' * 30 + '/', 7)

def compile(file):
    print_line()
    if os.system('g++ ./{0} -o temp/main {1} 2> temp/compile_log'.format(file, compile_parameter)):
        col_print('编译错误/', 1)
        print_line()
        return 1
    else:
        col_print("编译成功/", 2)
        print_line()
        return 0

def get_first_data(infile):
    os.system("cp temp/diff_log temp/first_diff_log")
    os.system("cp data/{0} temp/f_i_f".format(infile))
def get_process_pid(process_name):
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name() == process_name:
            return p.pid
    return -1
def get_process_memory(process_pid):
    p = psutil.Process(process_pid)
    mem_bytes, vmem_bytes = p.memory_info()
    mem_bytes /= (1024 * 1024)
    return mem_bytes
    
def judge():
    num = 0
    wa = False
    first = 233333333 
    the_time = 0.0
    unit_score = round(100 / len(jing), 1)
    last_score = 0
    print("序号\t结果\t时间\t得分")
    # 评测过程

    for j in jing:
        num = num + 1
        infile = j.join(input_name)
        outfile = j.join(output_name)
        ans = open("temp/temp.ans", "w+")
        ans.close()
        begin_time = time.time()
        return_run = os.system("ulimit -t {0} && ulimit -v {1} && temp/main < data/{2} > temp/temp.ans 2> temp/running_log".format(max_time, max_memory, infile))
        use_time = float(time.time() - begin_time) * 1000
        the_time += use_time
        return_diff = os.system("diff {0} temp/temp.ans data/{1} >> temp/diff_log".format(diff_parameter, outfile))
        # MLE
        if return_run == 35584:
            col_print("{0}\t".format(num), 7)
            col_print("MLE\t", 3)
            col_print("{0:.0f}ms\t{1:.0f}/".format(use_time, 0), 7)
            if wa == False:
                wa = True
                get_first_data(infile)
                first = num if first > num else first
        # TLE
        elif return_run == 35072:
            col_print("{0}\t".format(num), 7)
            col_print("TLE\t", 4)
            col_print("{0:.0f}ms\t{1:.0f}/".format(use_time, 0), 7)
            if wa == False:
                wa = True
                get_first_data(infile)
                first = num if first > num else first
        elif return_run == 0:
            # WA
            if return_diff:
                wa = True
                col_print("{0}\t".format(num), 7)
                col_print("WA\t", 1)
                col_print("{0:.0f}ms\t{1:.0f}/".format(use_time, 0), 7)
                if wa == False:
                    get_first_data(infile)
                    first = num if first > num else first
            # AC
            elif return_diff == 0:
                col_print("{0}\t".format(num), 7)
                col_print("AC\t", 2)
                col_print("{0:.0f}ms\t{1:.0f}/".format(use_time, unit_score), 7)
                last_score = last_score + unit_score
        # RE
        else:
            col_print("{0}\t".format(num), 7)
            col_print("RE\t", 5)
            col_print("{0:.0f}ms\t{1:.0f}/".format(use_time, unit_score), 7)
            if wa == False:
                wa = True
                get_first_data(infile)
                first = num if first > num else first

        # 获取运行时间

    # 输出信息
    col_print("总分: ", 7)
    col_print("{0:.0f}/".format(last_score), 2 if wa == 0 else 1)
    col_print("总时间: {0:.0f}ms/".format(float(the_time)), 7)
    if wa:
        print_line()
        print("你在第{0}个测试点出现了错误,下面是该点的输入数据:".format(first))
        os.system("cat temp/f_i_f")
        print_line()
        print("上面带减号\"-\"的是你的输出,下面带加号\"+\"的是答案输出，\"@@\"之间的数字表示行号:")
        with open("temp/first_diff_log") as dl:
            for line in dl:
                print(line, end='')
    print_line()

if __name__ == '__main__':
    if os.path.exists("./config.txt") == False:
        print("请填写config.txt")
        cf = open("config.txt", "w+")
        cf.write("File Name: \nInput Name (example#.in): \nOutput Name (example#.out): \n#s(1 2 3 4): \nmax running time(s): \nmax running memory(mb): ")
        cf.close()
        quit()
    if os.path.exists("data") == False:
        os.system("data")
        print("请向data文件夹放待测试数据")

    with open("./config.txt", "r+") as config:
        lst = list([])
        for line in config:
            temp = line.split(':')[1].strip()  # 去除两边空格
            lst.append(temp)
    file = lst[0]
    input_name = lst[1].split('#')
    output_name = lst[2].split("#")
    jing = lst[3].split(' ')
    max_time = int(lst[4])
    max_memory = int(lst[5]) * 1024 # kb
    print(input_name)
    print(output_name)
    print(jing)
    print(max_memory)
    print(max_time)

    os.system("rm -rf temp")
    os.system("mkdir temp")

    if compile(file):
        os.system('cat temp/compile_log')
        print_line()
    else :
        judge()
    os.system("rm -rf temp")
    quit()
