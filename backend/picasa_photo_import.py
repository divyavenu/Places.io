import gdata.photos.service
import gdata.media
import gdata.geo
import webbrowser
import httplib2
import argparse
import sys, os
from datetime import datetime, timedelta
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets
from oauth2client import tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SECRETPATH = "./backend"

def OAuth2Login(client_secrets, credential_store, email):
    """
    Creates OAuth2 creadentials for Google services, then uses them to create
    a PhotosService client for interacting with the Picasa API.
    Kudos: https://github.com/MicOestergaard/picasawebuploader/blob/master/main.py
    """
    scope='https://picasaweb.google.com/data/'
    user_agent='Places Dot IO'

    storage = Storage(credential_store)
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        flow = flow_from_clientsecrets(client_secrets, scope=scope)
        flow.user_agent = user_agent
        if flags:
            credentials = tools.run_flow(flow, storage, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, storage)
        """
        #Old authentication style
        flow = flow_from_clientsecrets(client_secrets, scope=scope, redirect_uri='urn:ietf:wg:oauth:2.0:oob')
        uri = flow.step1_get_authorize_url()
        webbrowser.open(uri)
        code = raw_input('Enter the authentication code: ').strip()
        credentials = flow.step2_exchange(code)
        """
        storage.put(credentials)

    if (credentials.token_expiry - datetime.utcnow()) < timedelta(minutes=5):
        http = httplib2.Http()
        http = credentials.authorize(http)
        credentials.refresh(http)

    gd_client = gdata.photos.service.PhotosService(source=user_agent,
                                               email=email,
                                               additional_headers={'Authorization' : 'Bearer %s' % credentials.access_token})
    return gd_client


def get_photo_url_and_geo(useremail):
    """
    Retrieves albums and photos from Google Photos via Picasa API, given a
    user's email address. Then attempts to print GPS info about each photo.
    """
    #XXX prompting for user email is clunky. Instead, should programmatically get user's email
    #after they login with Google account once we reach that point in frontend. 
    gd_client = OAuth2Login(os.path.join(SECRETPATH, "client_secret.json"),
                            os.path.join(SECRETPATH, "credential_store_" + useremail.split('@')[0]),
                            useremail)
    albums = gd_client.GetUserFeed(user=useremail)
    # List albums
    photos_list = []
    for album in albums.entry:
        photos = gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s?kind=photo' % (
                                   useremail, album.gphoto_id.text))
        # List photos in each album
        photocount = 0
        for photo in photos.entry:
            photo_obj = {}
            photo_obj["title"] = "PHOTO " + str(photocount)
            photocount += 1
            photo_obj["infotitle"] = photo.title.text
            photo_obj["infourl"] = photo.content.src
            # Add time if it exists. Use 2 formats, since not sure which 
            # will be easier to handle at the front-end later.
            if photo.exif.time is not None:
                epochtime = float(photo.exif.time.text)/1000
                photodt = datetime.fromtimestamp(epochtime)
                photo_obj["timestamp"] = photodt.strftime("%B %d, %Y")
                photo_obj["epochtime"] = epochtime
            else:
                photo_obj["timestamp"] = "No Time Data Found"
                photo_obj["epochtime"] = "No Time Data Found"
            # Add GPS information for photo if it exists
            if photo.geo.Point.pos:
                if photo.geo.Point.pos.text is not None:
                    latitude = photo.geo.latitude()
                    longitude = photo.geo.longitude()
                    photo_obj["latitude"] = latitude
                    photo_obj["longitude"] = longitude
                    # Only allow photo to be displayed on map if it has geo data
                    photos_list.append(photo_obj)
        return photos_list

def main():
    """
    Test driver to demonstrate functionality and basic results
    """
    results = get_photo_url_and_geo(useremail="ICC.Places.io@gmail.com")
    for result in results:
        print result

if __name__=="__main__":
    main()