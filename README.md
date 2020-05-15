# 这是一个易班校本化健康打卡的脚本

# 目录说明

- yiban

- - submit.py 自动打卡脚本

- - testSuccess.py 查看未打卡的任务

- - config.py 存放账号信息

- - utils.py 工具包,完成表单数据的提取和填充


# 安装
```shell script
git clone https://github.com/WadeStack/yiban.git
cd yiban
pip install requests
```

## 使用说明

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

- 将utils.py下的url换成刚复制的链接
   
#### 3.测试是否有未打卡的任务
```shell script
python testSuccess.py
```
#### 4.查看是否能提取数据
```shell script
python untils.py
```

5.打卡
```shell script
python submit.py
```




 
