from application import db
from application.models import Photo

db.drop_all()
db.create_all()

print("DB created.")