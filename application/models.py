from application import db

class Photo(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	useremail = db.Column(db.String(30))
	title = db.Column(db.String(75))
	infotitle = db.Column(db.String(75))
	infourl = db.Column(db.String(1600))
	latitute = db.Column(db.Numeric)
	longitute = db.Column(db.Numeric)
	timestamp = db.Column(db.String(50))
	epochtime = db.Column(db.Float)

	def __init__(self,useremail,title,infotitle,infourl,latitute,longitute,timestamp,epochtime):
		self.useremail = useremail
		self.title = title
		self.infotitle = infotitle
		self.infourl = infourl
		self.latitute = latitute
		self.longitute = longitute
		self.timestamp = timestamp
		self.epochtime = epochtime

