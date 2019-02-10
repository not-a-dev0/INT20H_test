from flask import render_template

from app import app
from app.dbmanager.photos_info_manager import PhotosInfoManager


@app.route('/')
def hello_world():
    photos_manager = PhotosInfoManager()
    photos = photos_manager.get_all_photos()
    return render_template('content.html', photos=photos)
