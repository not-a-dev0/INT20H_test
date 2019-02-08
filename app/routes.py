from app import app
from app.flickr.flickr_api import FlickrPhotosGetter


@app.route('/')
def hello_world():
    return FlickrPhotosGetter.get_photos()
    # return 'Hello World!'
