import gdata.photos.service
import gdata.media
import gdata.geo
import webbrowser
import httplib2
from datetime import datetime, timedelta
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets

def OAuth2Login(client_secrets, credential_store, email):
    """
    Creates OAuth2 creadentials for Google services, then uses them to create
    a PhotosService client for interacting with the Picasa API.
    Kudos: https://github.com/MicOestergaard/picasawebuploader/blob/master/main.py
    """
    scope='https://picasaweb.google.com/data/'
    user_agent='myapp'

    storage = Storage(credential_store)
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        flow = flow_from_clientsecrets(client_secrets, scope=scope, redirect_uri='urn:ietf:wg:oauth:2.0:oob')
        uri = flow.step1_get_authorize_url()
        webbrowser.open(uri)
        code = raw_input('Enter the authentication code: ').strip()
        credentials = flow.step2_exchange(code)
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
    useremail = raw_input("Please enter your Google email address: ")
    gd_client = OAuth2Login("./client_secret.json", "./credential_store", useremail)
    albums = gd_client.GetUserFeed(user=useremail)
    # List albums
    photos_list = []
    for album in albums.entry:
        photos = gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s?kind=photo' % (
                                   useremail, album.gphoto_id.text))
        # List photos in each album
        for photo in photos.entry:
            photo_obj = {}
            photo_obj["title"] = photo.title.text
            photo_obj["url"] = photo.content.src
            # Print GPS information for photo if it exists
            if photo.geo.Point.pos:
                if photo.geo.Point.pos.text is not None:
                    latitude = photo.geo.latitude()
                    longitude = photo.geo.longitude()
                    photo_obj["latitude"] = latitude
                    photo_obj["longitude"] = longitude
            photos_list.append(photo_obj)

def main():
    """
    Test driver to demonstrate functionality and basic results
    """
    results = get_photo_url_and_geo()
    for result in results:
        print result

if __name__=="__main__":
    main()