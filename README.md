# OALJ (OIer and ACMer's Local Judge)

LocalJudge [OALJ](https://github.com/OALJ/OALJ) developed by [kZime](https://github.com/kZime) && [Margatroid](https://github.com/enter-tainer) with ❤

example of `config.txt`:

``` test
File Name: test.cpp
Input Name (example#.in): test#.in
Output Name (example#.out): test#.ans
#(1 2 3 4): 0 1 2         //上文#所代表的数字/字符串
max running time(1(s)): 1
max running memory(256(mb)): 256
```
## 功能

目前支持的功能：判断 `AC`，`WA`，`TLE`，`MLE`，显示时间使用, 显示内存占用。

配合

## 使用方法

注意，暂时~~(未来八成也不会)~~不支持Windows系统。

### 安装:

执行`install.py`安照引导进行安装,**需要`sudo`权限。**

### 使用:

将数据放在data带评测文件目录内，并执行`oalj` 生成`config.txt`模板，然后进行填写。

之后执行`oalj`

配合`OJDK`后感受一下~

![cogs.gif](https://i.loli.net/2017/09/28/59cc8964c2589.gif)

### 其它特性

使用`oalj -r`可以删除当前目录下的`data`文件夹和`config.txt`文件。

使用`oalj -i [test.cpp]` 将忽略掉`config.txt` 中的`File name` , 直接对`[test.cpp]` 进行评测。

###  注意事项

<!---普通模式下出现`WA/TLE/MLE`后输出的错误点数据与正确数据上限为*15行*-->  

<!-- ~~使用`oalj -d`开启debug模式之后上限改为*30行*, 并且程序运行到第一个错误点会停下 ~~-->

```
TODO LIST:
  √√ 彩色输出
  √√ 显示时间占用
  -√ 显示内存占用
  -- 加入debug mode, 便于刷题时使用
```

