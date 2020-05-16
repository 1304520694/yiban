<h1 align="center">
  易班校本化健康打卡
  <br>
</h1>
<p align="center">
</p>

# 目录说明
```text
│  .gitignore
│  README.md            
|
└─yiban
    │  submit.py        自动打卡脚本
    │  testSuccess.py   查看未打卡的任务
    │  utils.py         工具包,完成表单数据的提取和填充
    │
    └─yiban
        │  config.py    存放账号信息
        │  __init__.py  存放基础类
        └─
```

# 安装
```shell script
git clone https://github.com/WadeStack/yiban.git
cd yiban
pip install requests
```

## :sparkles: 使用说明

#### 1.获取近几天的一次易班打卡登记表的转发审批表单的链接

1.登录易班app

2.点击易班校本化

3.点击每日健康打卡

4.点击右下角的已办

5.从已办列表选择最近一天的打卡登记表

6.点击我的反馈进入

7.点击最下面的转发审批表单，复制链接

#### 2. 修改配置参数

- 将config.py下的账号密码换成自己的

- 将config.py下的url换成刚复制的链接
  
#### 3.测试是否有未打卡的任务

```shell script
python testSuccess.py
```
#### 4.查看是否能提取数据
```shell script
python untils.py
```

#### 5.打卡
```shell script
python submit.py
```
> 打卡截图:通过打卡成功后生成的分享链接访问浏览器，然后截图


## 版本log

###### 2020-5-16 v0.1版本内容更新

1. 优化打卡提示

2. 生成打卡完成的分享链接


## 参考

### Reference project

- https://github.com/looyeagee/yiban_auto_submit 

- https://github.com/Avenshy/YibanCheckin

### Reference link

- https://looyeagee.cn/software/yiban

## 联系方式

- :email: hider2048@gmail.com