# DingTalkRobotTest
A sample for Dingtalk from robot sending message to dedicated person
本例是对钉钉开放平台机器人API发送消息的试验
本例共需要三个钉钉开放平台的参数，dingding_id，dingding_secret和dingding_userid
关于机器人的描述请参考：https://open.dingtalk.com/document/orgapp/robot-overview，申请机器人ＡＰＩ需要如下几个步骤：
1.注册钉钉开放平台，申请企业内部应用（在此场景下申请的是内部应用而不叫机器人）
2.添加成功后，在钉钉应用页(而不是机器人页）可以看到（我的是Infopush)
![新增的应用(https://github.com/windphone/DingTalkRobotTest/assets/99844467/f4e1338f-352a-4a1c-b856-94a5be2bfde8)
3.点击应用名可以看到AppKey和AppSecret（对应例子中的dingding_id和dingding_secret）
![application_id](https://github.com/windphone/DingTalkRobotTest/assets/99844467/48502828-5cc6-43fe-b960-04c2325ed6a4)
4.还有一个参数是机器人发送的对象，在例子中是本人申请的钉钉用户dingding_userid，这个参数需要到https://oa.dingtalk.com/contacts.htm#/contacts里查看
![UserID](https://github.com/windphone/DingTalkRobotTest/assets/99844467/e4123ff4-f67a-4f54-a106-1fff5b6981a0)
执行DingTalkTest.py即可实现发送钉钉信息到特定用户，其中自动生成的文件access_token_cache用来缓存发送消息时从钉钉获取的accessToken，默认2小时过期，程序会判断是否已经申请过并且没有过期，过期或者初次申请就会生成一个文件来保存该token以避免频繁进行申请。
