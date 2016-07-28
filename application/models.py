from application import db

class Photo(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	useremail = db.Column(db.String(30))
	title = db.Column(db.String(75))
	infotitle = db.Column(db.String(75))
	infourl = db.Column(db.String(1600))
	latitude = db.Column(db.Float)
	longitude = db.Column(db.Float)
	timestamp = db.Column(db.String(50))
	epochtime = db.Column(db.Float)

	def __init__(self,useremail,title,infotitle,infourl,latitude,longitude,timestamp,epochtime):
		self.useremail = useremail
		self.title = title
		self.infotitle = infotitle
		self.infourl = infourl
		self.latitude = latitude
		self.longitude = longitude
		self.timestamp = timestamp
		self.epochtime = epochtime

	def __repr__(self):
		retstr = "User: %s\nTitle:%s\nInfoTitle:%s\nInfoUrl:%s\n"
		retstr += "Latitude:%f\nLongitude:%f\nTimeStamp:%s\nEpochTime:%s\n"
		return retstr % (self.useremail, self.title, 
						 self.infotitle, self.infourl,
						 self.latitude, self.longitude,
						 self.timestamp, self.epochtime)
