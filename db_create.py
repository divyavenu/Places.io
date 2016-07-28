from application import db
from application.models import Photo

print "Dropping old DB"
db.drop_all()
print "Creating new DB"
db.create_all()

print("DB created.")