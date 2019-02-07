import requests
import json


class FlickrPhotosGetter:
    @staticmethod
    def get_photos():

        request_url = 'https://api.flickr.com/services/rest/?method=flickr.photos.getRecent&api_key=8ff7a9ee623f29351d684a2b6c7e4e14&per_page=10&format=json&nojsoncallback=1'

        api_key = '8ff7a9ee623f29351d684a2b6c7e4e14'

        args = dict()

        args["api_key"] = api_key
        args["format"] = 'json'
        args["nojsoncallback"] = 1

        response = requests.post(request_url, args)

        if response.status_code == 200:
            json_response = json.loads(response.text)

            print(json_response['photos'])