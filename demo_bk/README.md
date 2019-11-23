# 后端框架基本步骤

## 1 安装基本包
1. pip install flask_script  
2. pip install flask_migrate  
3. pip install MySQL-python  

## 2 数据库
python manage.py db init   初始化数据库,会创建一个migations文件夹,并且会在数据库中生成一个alembic_version表  
python manage.py db migrate  创建迁移历史  
python manage.py db upgrade  更新数据库  
