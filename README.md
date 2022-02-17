# thProxyHelper
东x网络自动签到程序

# 背景
东x网络为奇妙的地方，
每日签到可以获取部分流量奖励。
虽然奖励的数量不算很多，
但是俗话说聚沙成塔，有一点是一点嘛(才不是因为自己太懒)！

# 运行环境

有python3就行。

# 使用说明
* git 安装
> git clone https://github.com/DeSireFire/thProxyHelper.git

* 进入目录
> cd thProxyHelper

* 依赖安装
> pip install requests,chardet

* 添加账号密码到配置我呢见
> vi config.py

示例：
```text
email = '你的登录账号'
passwd = '你的登录密码'
```

* 运行
> python3 touhouHelper.py

# 温馨提示
```text
这是简单至极的自用开源程序，没有啥"售后".调吧调吧就会了.
如果有不错点子，欢迎提交pull requests.
```

# todo
* 定时任务
* 邮箱提醒
* 日志系统