from time import time

import requests


class FacePlusPlusApi:

    @staticmethod
    def detect_faces(urls):
        if len(urls) == 0:
            return list()

        request_url = 'https://api-us.faceplusplus.com/facepp/v3/detect'

        api_key = 'Mn2fDt_QekCPCyQaViVuwZ60E6jfzzXH'

        api_secret = '8OceY8JOsj8DWfc8PuDb6GZBbqdhhzZk'

        args = dict()

        args['api_key'] = api_key
        args['api_secret'] = api_secret

        args['return_attributes'] = 'emotion'

        results = list()

        start_time = time()

        for url in urls:
            args['image_url'] = url
            response = requests.post(request_url, args)
            emotions_on_photo = set()
            if response.status_code == 200:
                json_response = response.json()
                faces = json_response.get('faces')
                if faces is not None:
                    for face in faces:
                        attributes = face.get('attributes')
                        if attributes is not None:

                            emotions_on_face = attributes.get('emotion')
                            if emotions_on_face is not None:
                                for emotion in emotions_on_face:
                                    if emotions_on_face[emotion] >= 50:
                                        emotions_on_photo.add(emotion)
                                        break

            results.append((url, emotions_on_photo))

        end_time = time()

        return results
