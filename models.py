from exts import db

class User(db.Model):
    __tablename__  = "user"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100),nullable=False)
    image = db.Column(db.String(100),nullable=True)

    pwd = db.Column(db.String(100), nullable=False)