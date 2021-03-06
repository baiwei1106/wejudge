# WeJudge
_An Online Judge Work for Education_

程序设计在线评测辅助教学系统

演示网址：[https://oj.bnuz.edu.cn:8081/](https://oj.bnuz.edu.cn:8081/)；游客账号：guest，密码：wejudge


## 最新消息

2017年12月：WeJudge2.0于2017年9月发布第一个测试版本，目前仍在更新中。2.0项目已经申请著作权，并且决定暂时不开源，成立内部团队进行更新迭代。欢迎北师大珠海校区有意向加入项目组学习的同学们，发邮件到me#lanrongqi.com或者lancelrq#gmail.com联系我。岗位需求：Python后端开发、ReactJS前端开发、UI设计、产品运营。

2017年03月：WeJudge2.0正在开发中，此1.x版本不再更新；


## 介绍

　这是一个基于Python 2.7语言和django 1.8框架所开发的一套在线程序代码在线评测系统，支持C、C++、Java语言的评测。系统在支持代码评测的基础上，加入了在线教学管理和作业管理的功能，可以支持教学辅助使用。

　　我曾经也是ACM校队的一员，大一的时候游走于国内各大OJ，刷题，并且还去2015广东省赛打了个酱油拿了个铜牌。因某些原因退出校队后，在一次与导师的聊天中不谋而合，萌生了开发这个OJ的想法。


　　1.0版本于2015年5月开始着手研究，7月底开始开发，9月初第一版测试上线。经过一个学期的使用，发现存在的问题，决心对其代码重构，于2016年1月中旬开始重构系统代码，3月初完成并上线；而后又是一个学期的使用，师生反馈效果良好，并在16年暑假期间对其进行完善，最终于2016年8月20日发布正式版。历时1年零3个月。

　　**_从系统设计、数据建模，到代码编写、调试，再到部署、上线、维护，几乎都是我一个人搞定的。_**同时也感谢学校和老师的大力支持，提供硬件设施，以及项目经费等。 

　　构建这样一个完整的系统需要付出很多辛劳，但是也是一次非常好的学习机会，从中的受益无穷。因此，我也希望将这个源代码以GPL协议公开，以便有意愿想要学习或者想要二次开发的朋友能够作为一个参考。代码写的不好，文档也不多，请见谅，如果有什么问题，欢迎发邮件到 me#lanrongqi.com 联系我。（为啥是#号，咱都懂的哈）

## 环境需求

### 环境

Ubuntu + Nginx + Python2.7 + MySQL 5.6 ，建议用gunicorn来作为uWSGI管理器。

### 组件
Lo-runner (这是我fork并且修改过的，直接安装即可：https://github.com/LanceLRQ/Lo-runner/)

django >= 1.8

dbutil

django-mysqlpool

smtplib

PIL

xlrd

xlwt

还有记不住了...反正报什么错装什么呗，Lorun去我个人主页下的那个fork里边下或者去原作者那下都行。

查重用的是那个什么Laven...的请自行看源代码..

apt install indent （这个是支持那个代码格式化的命令行工具）

### 存储目录

请自己看 const.py 文件内的内容

### 目录详解

	<root>
	├ wejudge					WeJudge网站目录
	
		├ apps					├ Django APP目录，里边所有APP文件夹内的结构和Django的模板文件结构一致
			├ account				├ 用户账户模块
			├ asgn					├ 作业模块
			├ bnuzoj				├ 历史遗留的名称，网站的全站内容
			├ contest				├ 比赛模块
			├ cpanel				├ 管理模块
			├ datacenter			├ 数据分析模块（即将废弃）
			├ education				├ 教学中心模块以及教学资源库模块
			├ helper				├ 帮助页面模块
			├ oauth2				├ 内部Oauth2实现模块（服务端），不完善，未使用。
			├ problem				├ 题目库模块
			
		├ kernel				├ 业务逻辑核心代码
		
			├ general				├ 系统的核心功能以及常量放置点
				├ const.py				├ 系统公共常量
				├ error_const.py		├ 系统错误代码常量
				├ ESConnector.py		├ （北师珠）教务系统对接模块
				├ GeneralTools.py		├ 通用功能模块
				├ LocalStorage.py		├ 本地文件存储封装
				├ PagerProvider.py		├ 分页、分页按钮渲染提供程序
				├ RestStruct.py			├ RESTful消息体
				├ ViewerFramework.py 	├ Django模板渲染器封装
				├ WebConfiguration.py	├ 网站配置信息模块
			（其余目录含义同上apps文件夹）
			
		├ static				├ 静态文件，请使用Nginx等来管理，Django自带静态管理的似乎没有用
		├ templates				├ HTML模板代码（子目录含义同上apps文件夹）
		├ settings.py			├ Django配置文件
		├ urls.py				├ 中央路由配置
		├ wsgi.py				├ uswgi 入口
		
		
	├ JudgeService			评测机服务
	
		├ base.py				├ 基础功能模块
		├ config.py				├ 配置文件
		├ main.py				├ 入口
		├ master.py				├ 评测机模块
		├ master_func.py		├ 评测机模块
		├ tdmaker.py			├ 测试数据生成器模块
		├ master_func.py├ 测试数据生成器模块

## 版本说明

当前版本是V1.0.3，更新于2016年9月26日。		

## 作者简介

蓝荣祺

联系邮箱：me#lanrongqi.com 或者 lancelrq#gmail.com

微信：LanceLRQ


