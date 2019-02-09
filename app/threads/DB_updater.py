import threading
import time

from app.dbmanager.photos_info_manager import photos_info_db_manager
from app.flickr.flickr_api import FlickrPhotosGetter
from app.faceplusplus.faceplusplus_api import FacePlusPlusApi


class DBUpdater(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)

        self.name = name
        self.isWorking = True

    def run(self):
        """
        Get all photos from Flickr (from the album and by hashtag), compare it to photos from db,
        define which are new, then pass it to Face++ and push results to the DB
        """
        while self.isWorking:
            last_update_date = photos_info_db_manager.get_album_update_date()
            print(last_update_date)
            flickr_photos = FlickrPhotosGetter.get_all_photo_urls(last_update_date)

            print("\n\nflickr_photos:")
            print(flickr_photos)

            if len(flickr_photos) > 0:
                db_photos = photos_info_db_manager.get_photo_urls()
                print("\n\ndb manager:")
                print(db_photos)

                new_photos = flickr_photos.difference(db_photos)
                print("\n\nnew photos:")
                print(new_photos)

                if len(new_photos) > 0:
                    new_photos_info = FacePlusPlusApi.detect_faces(new_photos)
                    photos_info_db_manager.push_photos_info(new_photos_info)

            time.sleep(60 * 10)  # in seconds

    def stop(self):
        self.isWorking = False
