from application import db


class Data(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	latitute = db.Column(db.Numeric)
	longitute = db.Column(db.Numeric)
	date = db.Column(db.DateTime)

	def __init__(self,latitute,longitute,date):
		self.latitute = latitute
		self.longitute = longitute
		self.date = date
