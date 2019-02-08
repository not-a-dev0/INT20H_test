from flask import render_template

from app import app
from app.flickr.flickr_api import FlickrPhotosGetter
from app.faceplusplus.faceplusplus_api import FacePlusPlusApi

# from app.dbmanager.photos_info_manager import photos_info_db_manager


@app.route('/')
def hello_world():
    # return render_template('base.html', data=data)

    photo_urls = FlickrPhotosGetter.get_photo_urls()
    FacePlusPlusApi.detect_faces(photo_urls)

    return render_template('base.html')


@app.route('/flickr')
def flickr_api():
    FlickrPhotosGetter.get_photo_urls()
    return 'Flickr API works!'


@app.route('/faceplusplus')
def faceplusplus_api():
    FacePlusPlusApi.detect_faces(set())
    return 'FacePlusPlus API works!'
