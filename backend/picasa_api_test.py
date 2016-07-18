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


def main():
    """
    Retrieves albums and photos from Google Photos via Picasa API, given a
    user's email address. Then attempts to print GPS info about each photo.
    """
    #XXX prompting for user email is clunky. Instead, should programmatically get user's email
    #after they login with Google account once we reach that point in frontend. 
    username = raw_input("Please enter your Google email address: ")
    gd_client = OAuth2Login("./client_secret.json", "./credential_store", username)
    albums = gd_client.GetUserFeed(user=username)
    # List albums
    for album in albums.entry:
        print 'album title: %s, number of photos: %s, id: %s' % (album.title.text,
               album.numphotos.text, album.gphoto_id.text)
        photos = gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s?kind=photo' % (
                                   username, album.gphoto_id.text))
        # List photos in each album
        for photo in photos.entry:
            print '-'*45
            print 'Photo title:', photo.title.text
            print 'Photo url:', photo.content.src
            if photo.exif.make and photo.exif.model:
                camera = '%s %s' % (photo.exif.make.text, photo.exif.model.text)
                print '%s %s' % (photo.exif.make.text, photo.exif.model.text)
            # Print GPS information for photo if it exists
            if photo.geo.Point.pos:
                if photo.geo.Point.pos.text is not None:
                    print photo.geo.Point.pos.text
                    latitude = photo.geo.latitude()
                    longitude = photo.geo.longitude()
                    print "Lat:", latitude
                    print "Long:", longitude
                else:
                    print "No GPS data detected."


if __name__=="__main__":
    main()