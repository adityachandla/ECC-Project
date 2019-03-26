from auth import db

class UserModel(db.Model):
	index = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String,unique=True)
	password = db.Column(db.String)
	email = db.Column(db.String)
