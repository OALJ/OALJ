# OALJ (OIer and ACMer's Local Judge)

LocalJudge [OALJ](https://github.com/OALJ/OALJ) developed by [kZime](https://github.com/kZime) && [Margatroid](https://github.com/enter-tainer) with ❤

example of `config.json`:

``` test
{
  "Source": "test.cpp",
  "Input": "test#.in",
  "Output": "test#.ans",
  "#": [0, 1, 2, 3],
  "Time Limit": 1,
  "Memory Limit": 256
}
```
## 功能

目前支持的功能：判断 `AC`，`WA`，`TLE`，`MLE`，显示时间使用, 显示内存占用。

配合

## 使用方法

注意，暂时~~ (未来八成也不会) ~~不支持Windows系统。

### 安装:

执行`install.py`安照引导进行安装,**需要`sudo`权限。**

### 使用:

将数据放在data带评测文件目录内，并执行`oalj` 生成`config.json`模板，然后进行填写。

之后执行`oalj`

配合`OJDK`后感受一下~

![OALJ-DEMO](https://i.loli.net/2017/09/28/59cc95bd52d18.gif)

### config文档

使用[JSON](https://en.wikipedia.org/wiki/JSON)格式
([w3school](http://www.w3school.com.cn/json/index.asp))

注：
- 大小写敏感
- 缩进不强制
- "#"的值可为数字也可为字符串（用双引号扩起来），甚至两者交替： `"#": [1, 2, 3, "4", "5", "6", 7, "8", 9, 10]`
- "Source"项可忽略（当然，这要求你执行时添加'-i'参数，见下）

### 其它特性

使用`oalj -r`可以删除当前目录下的`data`文件夹和`config.txt`文件。

使用`oalj -i [test.cpp]` 将忽略掉`config.txt` 中的`File name` , 直接对`[test.cpp]` 进行评测。

###  注意事项

如果oalj抛出了未捕获的异常（就是那些英文的XxxxxError: xxxxxx什么的），请提出issue.
（如果您很强可以自己解决掉然后pull request）

<!---普通模式下出现`WA/TLE/MLE`后输出的错误点数据与正确数据上限为*15行*-->  

<!-- ~~使用`oalj -d`开启debug模式之后上限改为*30行*, 并且程序运行到第一个错误点会停下 ~~-->

```
TODO LIST:
  √√ 彩色输出
  √√ 显示时间占用
  -√ 显示内存占用
  -- 加入debug mode, 便于刷题时使用
  -- 加入`quite`模式, 只输出评测结果
  -- 加入评测服务器, 评测指定文件
```

