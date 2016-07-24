from application import db
from application.models import Photo

db.create_all()

print("DB created.")