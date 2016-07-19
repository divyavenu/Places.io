# Places.io
Introduction to Cloud Computing project


Using the photo’s EXIF geolocation metadata, present a user’s photo collection overlaid on a map with a date range filtering system

#### Run with Flask
Clone this repo to your local machine. In the top level directory, create a virtual environment:

$ virtualenv PlacesIO
$ source PlacesIO/bin/activate
Now install the required modules:

$ pip install -r requirements.txt
To play with the app right away, you can use a local database. Edit config.py by commenting out the AWS URL and uncomment this line:

SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/db_name'
Next run:

$ python db_create.py
And the tables are created. Now you can launch the app:

$ python application.py
And point your browser to http://0.0.0.0:5000




#### Website
To get the website working, you must have an "apiData.js" file in the website folder. This file will have the following keys as global variables:

GOOGLE_MAPS_API_KEY - (String) the Google Maps API key

Example: apiData.j
```
GOOGLE_MAPS_API_KEY = '1hfd3hjjdsd-23jk_33djfsje'; // your api key here
```

#### Backend
To run the sample script, you'll need to first install the gdata python client (https://github.com/google/gdata-python-client) then the "main" Google API python client by running:
```
pip install --upgrade google-api-python-client
```