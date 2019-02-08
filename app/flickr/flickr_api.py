import io

from flask import jsonify, send_file
import requests
import json

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

        response_album_photos = requests.post(request_url_get_album_photos, args)

        if response_album_photos.status_code == 200:
            # json_response_album_photos = json.loads(response_album_photos.text)
            json_response_album_photos = response_album_photos.json()
            print("\nalbum photos:")
            photos = json_response_album_photos["photoset"]["photo"]

            photo = photos[0]
            for photo in photos:
                print(photo)
                request_url_get_photo = "http://farm" + str(photo["farm"]) + ".staticflickr.com/" + str(
                    photo["server"]) + "/" + \
                                        str(photo["id"]) + "_" + str(photo["secret"]) + ".jpg"

                response_photo = requests.post(request_url_get_photo, args)
                if response_photo.status_code == 200:
                    photo_file = send_file(
                        io.BytesIO(response_photo.content),
                        mimetype='image/jpeg')
                    return photo_file

                # response_hashtag_photos = requests.post(request_url_get_hashtag_photos, args)
        #
        # if response_hashtag_photos.status_code == 200:
        #     # json_response_hashtag_photos = jsonify(xmltodict.parse())
        #     # print(json_response_hashtag_photos)
        #
        #     print("\n\nhashtag photos:")
        #     # print(response_hashtag_photos) - it's root object, print "<Response [200]>"
        #     # response_hashtag_photos.raw - return address of an object
        #     # response_hashtag_photos.json() - error
        #
        #     print("\n\ntext")
        #     print(response_hashtag_photos.text)
        #
        #     print("\n\ncontent")
        #     print(response_hashtag_photos.content)
        #
        #     # xmltodict.parse(response_hashtag_photos.content) same as xmltodict.parse(response_hashtag_photos.text)
        #
        #     xmldict_from_text = xmltodict.parse(response_hashtag_photos.text)
        #     print("\n\nxml dict from .text")
        #     # print(xmldict_from_text)
        #
        #     # xmldict_from_content = xmltodict.parse(response_hashtag_photos.content)
        #     # print("\n\nxml dict from .content")
        #     # print(xmldict_from_content)
        #
        #     print(xmldict_from_text["rsp"]["photos"])
