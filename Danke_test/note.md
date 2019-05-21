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
 
 Python manage.py makemigrations 应用名
 python manage.py migrate 应用名
 
 3.对于默认数据库，未来避免出现混乱，如果数据库没数据，可以删除
 自带sqllite3数据库，重新生成
 
 