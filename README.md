# Places.io
Introduction to Cloud Computing project


Using the photo’s EXIF geolocation metadata, present a user’s photo collection overlaid on a map with a date range filtering system

#### Run with Flask
Clone this repo to your local machine. In the top level directory, create a virtual environment:

$ virtualenv PlacesIO

$ source PlacesIO/bin/activate

Now install the required modules:

$ pip install -r requirements.txt

$ pip install --upgrade google-api-python-client

To play with the app right away, you can use a local database. Edit config.py by commenting out the AWS URL 

Modify config.py to include local/RDS database credentials in the format: Replace username and password
'mysql://username:password@localhost/db_name'


To run application: 

$ python db_create.py

$ python application.py

#### Create local database for testing
Create a mysql database called placesDB on local machine

#### Backend
To run the sample script, you'll need to first install the gdata python client (https://github.com/google/gdata-python-client) then the "main" Google API python client by running:
```
pip install --upgrade google-api-python-client
```
