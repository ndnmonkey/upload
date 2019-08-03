import os

SECRET_KEY =os.urandom(24)

basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(basedir,'files')  #连接上下层文件
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','tif','word'])  #允许上传的文件类型
MAX_CONTENT_LENGTH = 16 * 1024 * 1024 #最大传16M的文件

DIALECT = "mysql"
DRIVER = "mysqldb"
USERNAME = "root"
PASSWORD = '1234'
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "demo"

SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
"""指定一个名为SQLALCHEMY_DATABASE_URI的固定变量，注意是固定的写法"""
SQLALCHEMY_TRACK_MODIFICATIONS =False