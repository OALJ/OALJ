#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import sys
import time
import psutil
from subprocess import Popen
from colorama import init, Fore

# 编译选项
COMPILEARGV = "-DLOCAL"
# diff选项
DIFFARGVS = "-U 0 -b -B -w"
# 运行模式
Mode = "Normal"
ColorMap = {
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

def allClean():
    if os.path.isdir("/tmp/oalj"):
        os.system("rm -rf /tmp/oalj")
    if os.path.isfile("Diff.log"):
        os.remove("Diff.log")

def checkMode():
    global Mode
    global COMPILEARGV
    argvs = sys.argv
    if "-r" in argvs:
        allClean()
        if os.path.isdir("data"):
            os.rmdir("data &> /dev/null")
        if os.path.isfile("config.json"):
            os.remove("config.json")
        print("已经清除数据")
        quit()
    if "-q" in argvs:
        mode = "Lunatic"
        argvs.remove("-q")
    if "-i" in argvs:
        Problem["File"] = argvs[argvs.index("-i") + 1]
        argvs.remove(argvs[argvs.index("-i") + 1])
        argvs.remove("-i")
    for CppLevel in argvs:
        if CppLevel.find("-std=") != -1:
            COMPILEARGV += " " + CppLevel
    for OptimizeLevel in argvs:
        if OptimizeLevel.find("-O") != -1:
            COMPILEARGV += " " + OptimizeLevel

def colorPrint(content, col):
    global Mode
    if Mode == "Normal":
        print(ColorMap[col] + content, end="")

def linePrint():
    global Mode
    if Mode == "Normal":
        colorPrint('-' * 50 + '\n', 7)

def compileProgram(file):
    linePrint()
    CompileBegin = time.time()
    CompileReturn = os.system("g++ {0} -o /tmp/oalj/main {1} &> /tmp/oalj/Compile.log".format(file, COMPILEARGV))
    CompileTime = float(time.time() - CompileBegin)
    if CompileReturn:
        colorPrint("编译错误\n", 1)
        colorPrint("耗时: {0:.2f}s\n".format(CompileTime), 7)
        linePrint()
    else :
        colorPrint("编译成功\n", 2)
        colorPrint("耗时: {0:.2f}s\n".format(CompileTime), 7)
        linePrint()
    return CompileReturn
'''

{
    "File": "aplusb.cpp"
    "Name": "aplusb",
    "List": [1],
    "Input": ".in",
    "Output": ".ans",
    "MemoryLimit": 256,
    "TimeLimit": 1000
}

'''

def isdigit(x):
    try:
        x = int(x)
    except:
        return 0
    return 1


def get_process_memory(p):
    try:
        MemInfo = str(p.memory_info())
    except Exception:
        return 0
    RssBytes = int(MemInfo.split(',')[0].split('=')[-1])
    VmsBytes = int(MemInfo.split(',')[1].split('=')[-1])
    MemAll = float(RssBytes + VmsBytes) / 1024 / 1024
    return MemAll



def judge():
    global Problem
    global Mode
    DataName = Problem["Name"]
    Queue = Problem["List"]
    if len(Queue) == 2 and isdigit(Queue[0]) and isdigit(Queue[1]):
        Queue = list(range(Queue[0], Queue[1] + 1))
    Queue = list(map(str, Queue))
    Input = Problem["Input"]
    Output = Problem["Output"]
    MemoryLimit = Problem["MemoryLimit"]  # MB
    TimeLimit = Problem["TimeLimit"] # MS
    UnitScore = round(100 / len(Queue), 1)
    Score = 0
    Num = 0
    TimeAll = 0
    Ans = True
    if Mode == "Normal":
        colorPrint("序号\t结果\t时间\t内存\t返回值\t得分\n", 7)
    else:
        Result = ""
    for now in Queue: # str in Queue
        Num += 1
        InputFileName = DataName + now + Input
        OutputFileName = DataName + now + Output
        ProcessStatus = "Running"
        BeginTime = time.time()
        InputFile = open("data/%s" % InputFileName, "w")
        OutputFile = open("/tmp/oalj/Output", "w")
        ErrFile = open("/tmp/oalj/Running.log", "w")
        ChildProcess = Popen("/tmp/oalj/main", 0, None, stdin = InputFile, stdout = OutputFile, stderr = ErrFile)
        MaxMemoryUsed = 0
        p = psutil.Process(ChildProcess.pid)
        time.sleep(0.002)
        while ChildProcess.poll() == None:
            mem = get_process_memory(p)
            if time.time() - BeginTime > float(TimeLimit):
                ChildProcess.kill()
                ProcessStatus = "TLE"
            if mem * 1024 > MemoryLimit:
                ChildProcess.kill()
                ProcessStatus = "MLE"
            MaxMemoryUsed = max(MaxMemoryUsed, mem)
        TimeUsed = float(time.time() - BeginTime) * 1000
        ChildProcess.poll()
        ReturnCode = ChildProcess.returncode
        InputFile.close()
        OutputFile.close()
        ErrFile.close()
        MemoryUsed = MaxMemoryUsed
        TimeAll += TimeUsed
        DiffReturn = os.system("diff %s /tmp/oalj/Output data/%s >> /tmp/oalj/Diff.log" % (DIFFARGVS, OutputFileName))

        if ProcessStatus == "MLE":
            if Mode == "Lunatic":
                Result += "M"
                continue
            colorPrint(" %s\t" %str(Num), 7)
            colorPrint("MLE\t", 3)
            colorPrint("{0:.0f}ms\t{1:.2f}MB\t{2}\t{3:.0f}\n".format(TimeUsed, MemoryUsed, ReturnCode, 0), 7)
            if Ans:
                Ans = False
                os.system("cp data/%s /tmp/oalj/FalseInput" % InputFileName)
                os.system("cp /tmp/oalj/Output /tmp/oalj/FalseOutput")
                os.system("cp data/%s /tmp/oalj/FalseAns" % OutputFileName)




if __name__ == '__main__':
    allClean()
    Problem = config()
    checkMode()
    os.mkdir("/tmp/oalj")
    if compileProgram(Problem["File"]):
        if os.path.isfile("/tmp/oalj/Compile.log"):
            with open("/tmp/oalj/Compile.log", "r") as cl:
                for line in cl:
                    colorPrint(line + "\n", 1)
        else:
            colorPrint("没有评测代码， 请检查文件目录或者config.json\n", 1)
        linePrint()
    else :
        judge()
    allClean()
    quit()
