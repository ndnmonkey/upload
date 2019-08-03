from flask import Flask,request,render_template,redirect,url_for
import os
from werkzeug.utils import secure_filename
from exts import db
import config
import uuid
from models import User

basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(basedir,'static','images')  #连接上下层文件
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','tif','word'])  #允许上传的文件类型

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

def allowed_file(filename):
    #文件名有“.”且文件后缀在这个集合中则返回TRUE
    return '.' in filename and filename.strip().split('.')[1] in ALLOWED_EXTENSIONS

@app.route('/')
def hello_world():
    haha = "我是哈哈"
    return render_template('index.html',haha=haha)

@app.route('/register/', methods=['post','GET'])
def register():
    if request.method == "GET":
        return render_template('index.html')
    else:
        name = request.form.get('name')
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            uuid_str = str(uuid.uuid1())

            image_db = UPLOAD_FOLDER + os.sep + uuid_str + '.' + filename.split('.')[-1]
            file.save(image_db)
            #'images/zy.png'
            image_url = str('images' + os.sep + uuid_str + '.' + filename.split('.')[-1]).split('\\')
            image_url = '/'.join(image_url)
            print(image_url)
            user = User(name = name,image = image_url )
            db.session.add(user)
            db.session.commit()

            return render_template('uploadok.html',image_url=image_url)
        else:
            user = User(name = name )
            db.session.add(user)
            db.session.commit()
            return render_template('uploadok.html')

if __name__ == '__main__':
    app.run()
