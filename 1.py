import uuid,os

uuid_str = str(uuid.uuid1())
# print(uuid_str)
filename = "5.png"
basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(basedir,'files')  #连接上下层文件
image = UPLOAD_FOLDER + os.sep +uuid_str + '.' + filename.split('.')[-1]
print(image)


print(os.sep)

s = 'images\zy.png'
a = s.split('\\')
print('/'.join(a))