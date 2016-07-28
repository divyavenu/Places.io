# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://TeamHive:PlacesDotIO@flask-placesdotio.csjpunjsdlym.us-west-1.rds.amazonaws.com:3306/PlacesDB'

# Uncomment the line below if you want to work with a local DB
# 'mysql://username:password@localhost/db_name', db_name for our project is PlacesDB in my local system
#SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/PlacesDB'
SQLALCHEMY_DATABASE_URI = 'mysql://root:devlin112@localhost/PlacesDB'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'