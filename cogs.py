#!/usr/bin/env python3
import requests
import os

if __name__ == '__main__':
    id = (input("请输入题目编号(COGS): "))
    Url = 'http://cogs.pro/cogs/problem/problem.php?pid={0}'.format(id)
    Page = requests.get(Url)
    html = str(Page.content)
    try:
        CanBeSolve = html.split('badge badge-success\\\'>')[1].split('<')[0]
        print("此题是否可做: 裆燃啦!")
    except IndexError:
        print("ZLJ!此题不可做!")
        exit()

    DateCnt = int(html.split('badge badge-success\\\'>')[1].split('<')[0])
    DateName = html.split('<td><code>')[1].split('.')[0]
    Time = html.split(' s)')[0].split(' ms (')[1]
    Memory = html.split(' MB')[0].split('</th>\\n<td>')[-1]
    print("题目名称: {0}\n测试点数目: {1}".format(DateName, DateCnt))

    os.system("rm -rf data")
    os.system("mkdir data")
    for i in range(1, DateCnt + 1):
        print("正在下载第{0}组数据quq...".format(i))
        InputFlieName = DateName + str(i) + '.in'
        AnsFlieName = DateName + str(i) + '.ans'
        InputFlieUrl = "http://cogs.pro/cogs/problem/QuiXplorer/index.php?action=download&dir={0}&item={1}&order=name&srt=yes".format(DateName, InputFlieName)
        AnsFlieUrl = "http://cogs.pro/cogs/problem/QuiXplorer/index.php?action=download&dir={0}&item={1}&order=name&srt=yes".format(DateName, AnsFlieName)
        InputFile = requests.get(InputFlieUrl)
        AnsFile = requests.get(AnsFlieUrl)
        with open("data/{0}".format(InputFlieName), "wb") as line:
            line.write(InputFile.content)
        with open("data/{0}".format(AnsFlieName), "wb") as line:
            line.write(AnsFile.content)

    # config.txt

    # FileName
    FileName = "test.cpp"
    os.system("rm temp 2> /dev/null")
    os.system("ls > temp")
    with open("temp", "r") as ls:
        for line in ls:
            try:
                temp = line.split('.')[1]
            except IndexError:
                continue
            if temp == 'cpp\n':
                FileName = line.rstrip()
    os.system("rm temp 2> /dev/null")


    print("FileName: {0}\nTime: {1}\nMemory: {2}".format(FileName, Time, Memory))
    with open("config.txt", "w") as Config:
        Config.write("File Name: {0}\n".format(FileName))
        Config.write("Input Name: {0}\n".format(DateName + '#.in'))
        Config.write("Output Name: {0}\n".format(DateName + '#.ans'))
        temp = "#: "
        for i in range(1, DateCnt + 1):
            temp += str(i) + ' '
        Config.write(temp + '\n')
        Config.write("Max Running Time: {0}\n".format(Time))
        Config.write("Max Running Memory: {0}".format(Memory))

