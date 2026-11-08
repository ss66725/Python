# 260805 学习记录

暑期练习，共 7 个小程序。大部分是输入输出和基础语法练习。

| 文件 | 内容 |
|---|---|
| summer_practice1.py | 输入一个整数，判断它是质数还是合数（小于等于 1 的数两者都不是） |
| summer_practice2.py | 列表练习：计算一周销售总额，生成 7 个随机数，计算降水量的总和、最大值、最小值和平均值，按阈值筛选数据 |
| summer-practice3.py | 选择题判分：输入 20 个答案，与标准答案比对，答对 15 题及以上为通过 |
| summer-practice4.py | 输入名、中间名、姓，输出姓名缩写；输入一串数字，计算它们的和；另外定义了一个提取元音的函数 |
| summer_practice5.py | 统计字符串中每个字符出现的次数，找出最多和最少的字符；用字典把指定字符替换成其他字符（简单加密） |
| summer_practice6.py | 统计字符出现的次数；用字典做一个小菜单，可以查找、添加、删除名字 |
| summer_practice7.py | 面向对象：定义 `Pet` 类（名字、种类、年龄），并用 get/set 方法读写属性 |

**知识点**：`try/except`、列表推导式、随机数、字典统计、字典查找与增删、类与方法

## 期望输出

已测试的程序，示例输入和期望输出放在 [tests/](tests/) 文件夹中：`summer_practice1`、`summer-practice3`、`summer-practice4`、`summer_practice5`、`summer_practice6`。

没有自动测试的程序：

- `summer_practice2.py`：每次生成的随机数都不同，输出不固定。
- `summer_practice7.py`：输出里有对象的内存地址（如 `<__main__.Car object at 0x...>`），每次运行都不同。
