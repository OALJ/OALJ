#!/usr/bin/env python3
import requests
import os
import re

if __name__ == '__main__':
    id = (input('请输入题目编号(LOJ): '))
    Url = "https://loj.ac/problem/" + id
    DataUrl = "https://loj.ac/problem/{0}/testdata".format(id)
    Page = requests.get(Url)
    DataPage = requests.get(DataUrl)
    Html = str(Page.content.decode('utf-8'))
    DataHtml = str(DataPage.content.decode('utf-8'))
    CanBeSolve = Html.find('<a href=\"javascript:history.go(-1)\">')
    if CanBeSolve == -1:
        CanBeSolve = True
        print('此题是否可做: 裆燃啦!')
    else:
        CanBeSolve = False
        print('ZLJ!此题不可做!')
        exit()
    Memory = int(Html.split(' MiB</span>')[0].split('内存限制：')[-1])
    Time = int(Html.split(' ms</span>')[0].split('时间限制：')[-1])
    DataHtml = DataHtml.split('<tbody>')[1].split('</tbody>')[0]
    Reg = r'[0-9a-zA-z.]*\d+.in'
    DataList = re.findall(Reg, DataHtml)
    NameList = []
    for i in DataList:
        NameList.append(i.replace(".in",""))
    print("Time: {0} ms\nMemory: {1} MiB".format(Time, Memory))
    os.system("rm -rf data")
    os.system("mkdir data")
    os.system("cd data")
    os.system("wget -q -O {0}.zip  https://loj.ac/problem/{0}/testdata/download".format(id))
    os.system("unzip -q {0}.zip -d data/".format(id))
    os.system("rm {0}.zip".format(id))
    # CppFileName
    os.system("rm temp 2> /dev/null")
    os.system("ls > temp")
    CppFileName = "test.cpp"
    with open("temp", "r") as ls:
        for line in ls:
            try:
                temp = line.split('.')[1]
            except IndexError:
                continue
            if temp == 'cpp\n':
                CppFileName = line.rstrip()
    os.system("rm temp")
    with open("config.txt", "w") as Config:
        Config.write("File Name: {0}\n".format(CppFileName))
        Config.write("Input Name: {0}\n".format('#.in'))
        Config.write("Output Name: {0}\n".format('#.out'))
        temp = "#: "
        for i in NameList:
            temp += i + ' '
        Config.write(temp + '\n')
        Config.write("Max Running Time: {0}\n".format(Time))
        Config.write("Max Running Memory: {0}".format(Memory))
