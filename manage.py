from flask_script import Manager
from app import app
from exts import db
from flask_migrate import Migrate,MigrateCommand
from models import User

# migrate步骤1：
# 模型 -->  迁移 -->  表，分别用下面语句实现
# “python manage.py db init”   --> “python manage.py db migrate”   -->  “python manage.py db upgrade”
# 作用分别是1，初始化一个迁移环境。2，做出一个迁移表。3，映射成表。

# migrate步骤4：
#  “python manage.py db migrate”   -->  “python manage.py db upgrade”


manager = Manager(app)

migrate = Migrate(app,db)

manager.add_command("db",MigrateCommand)

if __name__ == '__main__':
    manager.run()