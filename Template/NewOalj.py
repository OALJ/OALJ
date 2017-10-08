#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import sys
import time
from colorama import init, Fore

# 编译选项
COMPILEARGV = "-DLOCAL -O2 -Wall"
# diff选项
DIFFARGV = "-U 0 -b -B -w"

color_map = {
    1: Fore.RED,
    2: Fore.GREEN,
    3: Fore.YELLOW,
    4: Fore.BLUE,
    5: Fore.MAGENTA,
    6: Fore.CYAN,
    7: Fore.WHITE
}

def config():
    if not os.path.exists("config.json"):
        print("请填写config.json")
        with open("config.json", "w+") as cf:
            cf.write("{\n"
                     "\t\"Name\": \"main.cpp\",\n"
                     "\t\"List\": [1, 10],\n"
                     "\t\"Input\": \".in\",\n"
                     "\t\"Output\": \".ans\",\n"
                     "\t\"MemoryLimit\": 256,\n"
                     "\t\"TimeLimit\": 1000"
                     "\n}")
        quit()
    with open("config.json", "r") as data:
        return json.load(data)

def all_clean():
    if os.path.isdir("/tmp/oalj"):
        os.system("rm -rf /tmp/oalj")
    if os.path.isfile("Diff.log"):
        os.remove("Diff.log")

def check_mode():
    mode = "Normal"
    if "-r" in sys.argv:
        all_clean()
        if os.path.isdir("data"):
            os.rmdir("data &> /dev/null")
        if os.path.isfile("config.json"):
            os.remove("config.json")
        print("已经清除数据")
        quit()
    if "-q" in sys.argv:
        mode = "Lunatic"
    if "-i" in sys.argv:
        Problem["Name"] = sys.argv[sys.argv.index("-i") + 1]
    return mode

def color_print(content, col):
    if Mode == "Normal":
        print(color_map[col] + content, end="")

def line_print():
    if Mode == "Normal":
        color_print('-' * 50 + '\n', 7)

def compile_program(file):
    line_print()
    CompileBegin = time.time()
    CompileReturn = os.system("g++ {0} -o /tmp/oalj/main {1} &> /tmp/oalj/Compile.log".format(file, COMPILEARGV))
    CompileTime = float(time.time() - CompileBegin)
    if CompileReturn:
        color_print("编译错误\n", 1)
        color_print("耗时: {0:.2f}s\n".format(CompileTime), 7)
        line_print()
    else :
        color_print("编译成功\n", 2)
        color_print("耗时: {0:.2f}s\n".format(CompileTime), 7)
        line_print()
    return CompileReturn

def judge():
    print(FileName)




if __name__ == '__main__':
    all_clean()
    Problem = config()
    Mode = check_mode()
    FileName = Problem["Name"]
    os.mkdir("/tmp/oalj")
    if compile_program(Problem["Name"]):
        if os.path.isfile("/tmp/oalj/Compile.log"):
            with open("/tmp/oalj/Compile.log", "r") as cl:
                for line in cl:
                    color_print(line + "\n", 1)
        else:
            color_print("没有评测代码， 请检查文件目录或者config.json\n", 1)
        line_print()
    else :
        judge()
    all_clean()
    quit()