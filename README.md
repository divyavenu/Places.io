# Places.io
Introduction to Cloud Computing project


Using the photo’s EXIF geolocation metadata, present a user’s photo collection overlaid on a map with a date range filtering system

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