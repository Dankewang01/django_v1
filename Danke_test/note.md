手动编写视图
实验目的
1.业务处理  
2.返回response子类 
a拿到模板 b数据  c环境变量 d返回 

分析

render(request, template_name, context=None,
           context_instance=_context_instance_undefined,
           content_type=None, status=None, current_app=_current_app_undefined,
           dirs=_dirs_undefined, dictionary=_dictionary_undefined,
           using=None):
           
           
models 模型
-DRM

-Django 链接数据库
   -自带默认数据库sqllite3
       -关系型数据库
       -轻量级
   -开发使用sqllite3 部署使用mysql等
   
   
 数据库迁移
 
 1.在命令行中，生成数据迁移的语句
 python3 manage.py makemigrations
 
 2.迁移数据
 
 python manage.py migrate
 
 ps: 迁移中会报错，尝试强制迁移
 
 #强制迁移
 
 强制准备：Python manage.py makemigrations 应用名 
 
 执行迁移：python manage.py migrate 应用名
 
 3.对于默认数据库，未来避免出现混乱，如果数据库没数据，可以删除
 自带sqllite3数据库，重新生成
 
 
 #启用脚本查询数据库
 
 1.进入虚拟环境 ，进入项目文件夹，执行命令python manage.py  shell打开编辑界面
 
 (test) G:\001-Python\clone_project\django_v1\Danke_test>python manage.py  shell
 
 2. 导入APP（test_app）里 Models XX表(Teacher)
 from test_app.models import Teacher
 
 3.数据库增删改查
 
 #查询所有
>>> a=Teacher.objects.all()
>>> a
[<Teacher: Danke>, <Teacher: XiaoMing>, <Teacher: XiaoLi>]

Teacher.objects.all().values('name')    #只取user列
 #取出id和user列，并生成一个列表
 a=Teacher.objects.all().values_list('name','age')
 >>> a
 [('Danke', 19), ('XiaoMing', 33), ('XiaoLi', 19)]

#查询age=19、name=Danke的值
Teacher.objects.get(age=19)
Teacher.objects.get(name='Danke')
