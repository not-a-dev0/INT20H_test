import requests

class FlickrPhotosGetter:

    ALBUM_OWNER = "144522605@N06"
    ALBUM_ID = "72157674388093532"
    API_KEY = "8ff7a9ee623f29351d684a2b6c7e4e14"

    @staticmethod
    def get_all_photo_urls(from_date):
        all_photos = FlickrPhotosGetter.get_photo_urls_from_album(from_date)
        all_photos.update(FlickrPhotosGetter.get_photo_urls_from_tag(from_date))
        return all_photos

    @staticmethod
    def get_photo_urls_from_album(from_date):
        last_update_date = int(FlickrPhotosGetter.get_album_update_date())
        if last_update_date > from_date:
            request_url_get_album_photos = "https://api.flickr.com/services/rest/?method=flickr.photosets.getPhotos&api_key=" + \
                                           FlickrPhotosGetter.API_KEY + \
                                           "&format=json&nojsoncallback=1&photoset_id=" + FlickrPhotosGetter.ALBUM_ID + \
                                           "&user_id=" + FlickrPhotosGetter.ALBUM_OWNER
            return FlickrPhotosGetter.get_photo_urls("photoset", request_url_get_album_photos)
        else:
            return set()

    @staticmethod
    def get_photo_urls_from_tag(from_date):
        all_tag_photos = set()
        page = 1
        request_url_get_hashtag_photos = "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=" + \
                                         FlickrPhotosGetter.API_KEY + \
                                         "&tags=int20h&format=json&nojsoncallback=1&min_upload_date=" + str(from_date)  # nature - for testing result parsing on more than 100 results
        next_page_photos = FlickrPhotosGetter.get_photo_urls("photos", request_url_get_hashtag_photos)
        all_tag_photos.update(next_page_photos)
        page += 1
        while len(next_page_photos) > 0:
            print(page)
            request_url_get_hashtag_photos = "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=" + \
                                             FlickrPhotosGetter.API_KEY + \
                                             "&tags=int20h&format=json&nojsoncallback=1&min_upload_date=" + str(from_date) + \
                                             "&page=" + str(page)
                                                    # nature - for testing result parsing on more than 100 results
            next_page_photos = FlickrPhotosGetter.get_photo_urls("photos", request_url_get_hashtag_photos)
            all_tag_photos.update(next_page_photos)
            page += 1

        return all_tag_photos

    @staticmethod
    def get_photo_urls(json_object_name, request_url):
        all_photos = set()
        args = dict()
        response_hashtag_photos = requests.post(request_url, args)
        print(response_hashtag_photos.json())

        if response_hashtag_photos.status_code == 200:
            json_response_hashtag_photos = response_hashtag_photos.json()
            hashtag_photos = json_response_hashtag_photos[json_object_name]["photo"]
            for photo in hashtag_photos:
                photo_link = "http://farm" + str(photo["farm"]) + ".staticflickr.com/" + str(
                    photo["server"]) + "/" + \
                             str(photo["id"]) + "_" + str(photo["secret"]) + ".jpg"
                # print(photo_link)
                all_photos.add(photo_link)

        print(all_photos)
        return all_photos


    @staticmethod
    def get_album_update_date():
            album_info = FlickrPhotosGetter.get_album_info()
            date_update = (album_info['photoset'])['date_update']
            return date_update


    @staticmethod
    def get_album_info():
        request_url_get_album_info = "https://api.flickr.com/services/rest/?method=flickr.photosets.getInfo&api_key=" + \
                                       FlickrPhotosGetter.API_KEY + \
                                       "&format=json&nojsoncallback=1&photoset_id=" + FlickrPhotosGetter.ALBUM_ID + \
                                       "&user_id=" + FlickrPhotosGetter.ALBUM_OWNER
        response_album_info = requests.post(request_url_get_album_info)
        print(response_album_info)
        if response_album_info.status_code == 200:
            return response_album_info.json()
        return None