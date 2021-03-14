# Locustperformancetesting

#### 介绍
Locust1.3.0接口性能测试v1.0版

#### 软件架构
使用Locust1.3.0 + lxml实现 common目录中config.py配置文件，对测试地址和目录路径进行的配置，根据自身需求可以进行一些添加修改。
database目录：用来保存测试时需要的数据，数据来源可以是数据库、文本等。 
debug目录：写代码过程中调试时用 
LocustFiles目录中写入需要进行并发测试的接口 
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

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
