#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
import sys
import time
import colorama 
import subprocess
import psutil
from subprocess import Popen
from colorama import init, Fore
# 编译选项
compile_parameter = "-DLOCAL -O2 -Wall"
# diff选项
diff_parameter = "-U 0 -b -B -w"

color_map = { 1:Fore.RED, 2:Fore.GREEN, 3:Fore.YELLOW, 4:Fore.BLUE, 5:Fore.MAGENTA, 6:Fore.CYAN, 7:Fore.WHITE}
def col_print(str, col):
    print(color_map[col] + str, end = "")

def print_line():
    col_print('-' * 50 + '\n', 7)

def compile(file):
    print_line()
    compile_begin = time.time()
    if os.system('g++ ./{0} -o temp/main {1} 2> temp/compile_log'.format(file, compile_parameter)):
        col_print('编译错误\n耗时: {0:.2f}s\n'.format(float(time.time() - compile_begin)), 1)
        print_line()
        return 1
    else:
        col_print("编译成功\n耗时: {0:.2f}s\n".format(float(time.time() - compile_begin)), 2)
        print_line()
        return 0

def get_first_data(infile):
    os.system("cp temp/diff_log temp/first_diff_log")
    os.system("cp data/{0} temp/f_i_f".format(infile))
def get_process_memory(p):
    try:
        mem_info = str(p.memory_info())
    except Exception:
        return 0
    rss_bytes = int(mem_info.split(',')[0].split('=')[-1])
    vms_bytes = int(mem_info.split(',')[1].split('=')[-1])
    mem_all = float(rss_bytes + vms_bytes) / 1024 / 1024
    return mem_all
def judge():
    num = 0
    wa = False
    first = 233333333 
    the_time = 0.0
    unit_score = round(100 / len(jing), 1)
    last_score = 0
    print("序号\t结果\t时间\t内存\t返回值\t得分")
    # 评测过程
    for j in jing:
        num = num + 1
        infile = j.join(input_name)
        outfile = j.join(output_name)
        process_status = "Running"
        begin_time = time.time()
        input_file = open("data/{0}".format(infile), "r")
        output_file = open("temp/temp.ans", "w")
        err_file = open("temp/running_log", "w")
        child_process = Popen("temp/main", 0, None, stdin = input_file, stdout = output_file, stderr = err_file)
        max_memory_used = 0
        p = psutil.Process(child_process.pid)
        while child_process.poll() == None:
            mem = get_process_memory(p)
            if time.time() - begin_time > float(max_time) / 1000:
                child_process.kill()
                process_status = "TLE"
            if mem * 1024 > max_memory:
                child_process.kill()
                process_status = "MLE"
            max_memory_used = max(max_memory_used, mem)
        child_process.poll()
        return_run = child_process.returncode
        input_file.close()
        output_file.close()
        err_file.close()
        # return_run = os.system("ulimit -t {0} && ulimit -v {1} && temp/main < data/{2} > temp/temp.ans 2> temp/running_log".format(max_time, max_memory, infile))
        use_time = float(time.time() - begin_time) * 1000
        memory_used = max_memory_used
        the_time += use_time
        return_diff = os.system("diff {0} temp/temp.ans data/{1} >> temp/diff_log".format(diff_parameter, outfile))
        # MLE
        if process_status == "MLE":
            col_print("{0}\t".format(num), 7)
            col_print("MLE\t", 3)
            col_print("{0:.0f}ms\t{1:.2f}MB\t{2}\t{3:.0f}\n".format(use_time, memory_used, return_run, 0), 7)
            if wa == False:
                wa = True
                get_first_data(infile)
                first = num if first > num else first
        # TLE
        elif process_status == "TLE":
            col_print("{0}\t".format(num), 7)
            col_print("TLE\t", 4)
            col_print("{0:.0f}ms\t{1:.2f}MB\t{2}\t{3:.0f}\n".format(use_time, memory_used, return_run, 0), 7)
            if wa == False:
                wa = True
                get_first_data(infile)
                first = num if first > num else first
        elif return_run == 0:
            # WA
            if return_diff:
                col_print("{0}\t".format(num), 7)
                col_print("WA\t", 1)
                col_print("{0:.0f}ms\t{1:.2f}MB\t{2}\t{3:.0f}\n".format(use_time, memory_used, return_run, 0), 7)
                if wa == False:
                    wa = True
                    get_first_data(infile)
                    first = num if first > num else first
            # AC
            elif return_diff == 0:
                col_print("{0}\t".format(num), 7)
                col_print("AC\t", 2)
                col_print("{0:.0f}ms\t{1:.2f}MB\t{2}\t{3:.0f}\n".format(use_time, memory_used, return_run, 10), 7)
                last_score = last_score + unit_score
        # RE
        else:
            col_print("{0}\t".format(num), 7)
            col_print("RE\t", 5)
            col_print("{0:.0f}ms\t{1:.2f}MB\t{2}\t{3:.0f}\n".format(use_time, memory_used, return_run, 0), 7)
            if wa == False:
                wa = True
                get_first_data(infile)
                first = num if first > num else first
        # 获取运行时间



    # 输出信息
    col_print("总分: ", 7)
    col_print("{0:.0f}\n".format(last_score), 2 if wa == 0 else 1)
    col_print("总时间: {0:.0f}ms\n".format(float(the_time)), 7)
    if wa:
        print_line()
        print("你在第{0}个测试点出现了错误,下面是该点的输入数据:".format(first))
        cnt = 0
        with open("temp/f_i_f") as dl:
            for line in dl:
                if cnt >= (30):
                    print('...')
                    break
                print(line, end='')
                cnt += 1
        col_print('\n', 7)
        print_line()
        print("上面带减号\"-\"的是你的输出,下面带加号\"+\"的是答案输出，\"@@\"之间的数字表示行号:")
        cnt = 0
        with open("temp/first_diff_log") as dl:
            for line in dl:
                if cnt >= (30):
                    print('...')
                    break
                print(line, end='')
                cnt += 1
    print_line()

if __name__ == '__main__':
    init(autoreset=True)
    if len(sys.argv) == 2:
        if sys.argv[1] == '-r':
            os.system("rm -rf ./data")
            os.system("rm ./config.txt")
            print("已清除data文件夹和config.txt")
            exit(0)
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
    # print(input_name)
    # print(output_name)
    # print(jing)
    # print(max_memory)
    # print(max_time)

    os.system("rm -rf temp")
    os.system("mkdir temp")

    if compile(file):
        os.system('cat temp/compile_log')
        print_line()
    else :
        judge()
    os.system("rm -rf temp")
    quit()
