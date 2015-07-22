
#[learn_models](https://github.com/Dstone11/learn_models)  
基于Python的Django模型，利用Bootstrap3前端框架，实现常用的基本功能，如增删改查、批量删除以及分页等，数据库使用Django自带的轻量级SQLite，具体实现过程如下：<br>
##安装和运行
本demo运行在Python2.7+Django1.8.3+Bootstrap 3 的框架上，操作系统为win7.<br> 
在安装Python2.7时，请注意勾选环境配置工具包，默认是关闭的，如果没设置，安装之后可手动添加"…/Python27/Scripts"到环境变量的path中。如果配置成功，进入cmd后，任何路径输入Python，可查看Python的版本信息：<br>
直接下载：[get-pip.py](https://bootstrap.pypa.io/get-pip.py) 然后运行在终端运行（其实Python2.7已经集成有pip的，有的话忽略，可以在Scripts文件中查看） 
```python
python get-pip.py
```
就可以安装 pip,再通过pip安装Django
```pip
pip install Django
```
在python终端环境输入
```python
import django
django.get_version()
```
查看输出的Django信息，验证安装成功！<br>
Clone或Download 该测试demo，然后cd到learn_models目录下，可以看到有manage.py，这正是运行的管理器，先同步数据库，然后运行
```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
打开<http://127.0.0.1:8000/q/>即可运行。<br>
具体实现过程请参考我的博客[正在写中……](http://www.cnblogs.com/dingshilei/)




