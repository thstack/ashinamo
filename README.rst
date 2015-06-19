=========
Ashinamo
=========

阿史纳摩，唐朝开国名将，李世民甚爱。事两主，两主皆悦。

这个项目不仅仅是个 C/S项目，还是个B/S项目，通过完整的技术实践，
简单实现服务器集群的监控，并通过 Web 界面动态展示波浪线变化。
整个项目基于 Python + Django + Nginx + Twisted 组合进行开发。


使用 Ashinamo
---------------

* 下载 Ashinamo 项目的源代码：

    $ git clone https://github.com/thstack/ashinamo


* 安装 Ashinamo 项目的依赖环境包：

    $ cd ashinamo
    $ pip install -r requirements.txt

* 同步数据库表结构：

    $ python manage.py migrate

* 运行 Ashinamo：

    $ python manage.py runserver 0.0.0.0:8000


代码规范检测
------------

* 检测代码是否符合规范

    $ tox
