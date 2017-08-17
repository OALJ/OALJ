#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
import time

# 编译选项
compile_parameter = "-DLOCAL -O2 -g -Wall"
# diff选项
diff_parameter = "-U 0 -b -B -w"

def ___():
    print('-' * 30)

def compile(file):
    ___()
    if os.system('g++ ./{0} -o temp/main {1} 2> temp/compile_log'.format(file, compile_parameter)):
        print('编译错误!!')
        ___()
        return 1
    else:
        print("编译成功")
        ___()
        return 0

def judge():
    num = 0
    wa = False
    first = 233333333
    the_time = 0.0
    unit_score = round(100 / len(jing), 1)
    last_score = 0
    print("序号    结果      时间      得分")
    # 评测过程

    for j in jing:
        num = num + 1
        infile = j.join(input_name)
        outfile = j.join(output_name)
        begin_time = time.time()
        return_num = os.system("ulimit -t {0} && ulimit -v {1} && temp/main < data/{2} > temp/temp.ans 2> temp/running_log".format(max_time, max_memory, infile))
        use_time = float(time.time() - begin_time) * 1000
        # MLE
        if return_num == 35584:
            print(" {0}     MLE   {1:6.0f}ms      {2:.0f}".format(num, float(time.time() - begin_time) * 1000, unit_score))
        # TLE
        elif return_num == 35072:
            print(" {0}     TLE   {1:6.0f}ms      {2:.0f}".format(num, float(time.time() - begin_time) * 1000, unit_score))
        # WA
        elif os.system("diff {0} temp/temp.ans data/{1} >> temp/diff_log".format(diff_parameter, outfile)):
            print(" {0}      WA   {1:6.0f}ms      {2:.0f}".format(num, float(time.time() - begin_time) * 1000, unit_score))
            if wa == False:
                wa = True
                os.system("cp temp/diff_log temp/first_diff_log")
                os.system("cp temp/temp.ans temp/w_a")
                os.system("cp data/{0} temp/f_i_f".format(infile))
                os.system("cp data/{0} temp/f_o_f".format(outfile))
                first = num if first > num else first
        # AC
        else:
            print(" {0}      AC   {1:6.0f}ms      {2:.0f}".format(num, float(time.time() - begin_time) * 1000, unit_score))
            last_score = last_score + unit_score
        # 获取运行时间
        the_time = the_time + (time.time() - begin_time) * 1000

    # 输出信息
    print("总分: {0:.0f}\n总时间: {1:.0f}ms".format(last_score + 0.5, float(the_time)))
    if wa:
        ___()
        print("你在第{0}个测试点出现了错误,下面是该点的输入数据:".format(first))
        os.system("cat temp/w_a")
        ___()
        print("上面带减号\"-\"的是你的输出,下面带加号\"+\"的是答案输出，\"@@\"之间的数字表示行号:")
        with open("temp/first_diff_log") as dl:
            for line in dl:
                print(line, end='')
    ___()

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


    os.system("rm -rf temp")
    os.system("mkdir temp")

    if compile(file):
        os.system('cat temp/compile_log')
        ___()
    else :
        judge()
    os.system("rm -rf temp")
    quit()
