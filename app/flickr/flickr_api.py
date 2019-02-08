import requests

import xmltodict as xmltodict


class FlickrPhotosGetter:

    @staticmethod
    def get_photos():

        album_owner = "144522605@N06"
        album_id = "72157674388093532"

        request_url_get_album_photos = "https://api.flickr.com/services/rest/?method=flickr.photosets.getPhotos&api_key=8ff7a9ee623f29351d684a2b6c7e4e14&format=json&nojsoncallback=1&photoset_id=" + album_id
        "&user_id=" + album_owner

        request_url_get_hashtag_photos = "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=8ff7a9ee623f29351d684a2b6c7e4e14&tags=int20h"  # nature - for testing result parsing on more than 100 results

        # should use paggination, because default perpage = 100, and results for hashtag searching could be more than that

        api_key = "8ff7a9ee623f29351d684a2b6c7e4e14"

        args = dict()

        # args["api_key"] = api_key
        # args["format"] = 'json'
        # args["nojsoncallback"] = 1
        #
        # # args["method"] = "flickr.photosets.getPhotos"
        # # args["method"] = "flickr.photos.search"
        #
        #
        # args["photoset_id"] = "72157674388093532"
        #
        # args["user_id"] = "144522605@N06"

        # response = requests.post(request_url, args)

        all_photos = set()

        response_album_photos = requests.post(request_url_get_album_photos, args)

        if response_album_photos.status_code == 200:
            json_response_album_photos = response_album_photos.json()
            photos = json_response_album_photos["photoset"]["photo"]

            for photo in photos:
                photo_link = "http://farm" + str(photo["farm"]) + ".staticflickr.com/" + str(
                    photo["server"]) + "/" + \
                             str(photo["id"]) + "_" + str(photo["secret"]) + ".jpg"
                # print(photo_link)
                all_photos.add(photo_link)

        response_hashtag_photos = requests.post(request_url_get_hashtag_photos, args)

        if response_hashtag_photos.status_code == 200:

            xmldict_from_text = xmltodict.parse(response_hashtag_photos.text)

            print(xmldict_from_text["rsp"]["photos"])
            # number_of_pages = xmldict_from_text["rsp"]["photos"]["@pages"]
            hashtag_photos = xmldict_from_text["rsp"]["photos"]["photo"]
            for photo in hashtag_photos:
                photo_link = "http://farm" + str(photo["@farm"]) + ".staticflickr.com/" + str(
                    photo["@server"]) + "/" + \
                             str(photo["@id"]) + "_" + str(photo["@secret"]) + ".jpg"
                # print(photo_link)
                all_photos.add(photo_link)

        print(all_photos)
        return all_photos
