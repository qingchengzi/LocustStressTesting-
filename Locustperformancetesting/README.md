# Locustperformancetesting

#### 介绍
Locust1.3.0接口性能测试v1.0版

#### 软件架构
使用Locust1.3.0 + lxml实现 common目录中config.py配置文件，对测试地址和目录路径进行的配置，根据自身需求可以进行一些添加修改。
database目录：用来保存测试时需要的数据，数据来源可以是数据库、文本等。 
debugcode目录：临时调试代码使用
LocustFiles目录:具体需要进行并发测试的接口 
logs日志目录 
util工具目录 
main_locust_run.py执行入口，执行该文件选择策略后，即可进行性能测试。

#### 安装教程

1.  下载Locust1.3.0 
2.  lxml


#### 使用说明

main_locust_run.py 运行入口
LocustFiles目录-->WithHtmlParsing.py参考官网网站写的一个实例.
locust和lxml配合使用，通过lxmp获取指定url页面中a标签中href属性的值，作为下一个请求的url进行压测


