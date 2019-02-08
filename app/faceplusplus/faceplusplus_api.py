from time import time

import requests


class FacePlusPlusApi:

    @staticmethod
    def detect_faces(urls):

        urls = set()
        urls.add("http://farm6.staticflickr.com/5747/30323171370_edf2e3f800.jpg")
        urls.add("http://farm8.staticflickr.com/7913/46095821035_ccca40bf16.jpg")
        urls.add("http://farm8.staticflickr.com/7837/40045107223_b75ba4842f.jpg")
        urls.add("http://farm8.staticflickr.com/7847/46095820685_ef299105dd.jpg")
        urls.add("http://farm5.staticflickr.com/4905/46095820435_a3b1d83a75.jpg")
        # urls.add("http://farm8.staticflickr.com/7890/46095820285_7b2b5ba9ff.jpg")
        # urls.add("http://farm8.staticflickr.com/7886/46095820085_8c577dd37c.jpg")
        # urls.add("http://farm8.staticflickr.com/7879/46095819905_676d2ebd1c.jpg")
        # urls.add("http://farm8.staticflickr.com/7873/46095819715_6dfb5285bd.jpg")
        # urls.add("http://farm5.staticflickr.com/4902/46095819435_081242cdab.jpg")
        # urls.add("http://farm5.staticflickr.com/4895/46095819215_4e18dc7813.jpg")
        # urls.add("http://farm5.staticflickr.com/4904/46095819035_71403a5edf.jpg")
        # urls.add("http://farm5.staticflickr.com/4911/46095818825_fb667a94df.jpg")
        # urls.add("http://farm5.staticflickr.com/4858/46095818645_0690320720.jpg")
        # urls.add("http://farm5.staticflickr.com/4869/46095818355_be22b40d19.jpg")
        # urls.add("http://farm5.staticflickr.com/4861/40045103113_62fb16de82.jpg")
        # urls.add("http://farm8.staticflickr.com/7925/46095817955_8315c57373.jpg")
        # urls.add("http://farm8.staticflickr.com/7812/40045102573_8394b3d5fb.jpg")
        # urls.add("http://farm8.staticflickr.com/7881/46095817625_dc903c393c.jpg")
        # urls.add("http://farm5.staticflickr.com/4890/40045102033_0dfe350e9b.jpg")
        # urls.add("http://farm8.staticflickr.com/7859/46285665354_98e0b4bfe6.jpg")
        # urls.add("http://farm5.staticflickr.com/4859/46095816925_311a9439cd.jpg")
        # urls.add("http://farm8.staticflickr.com/7901/46285664974_dd670c3a86.jpg")
        # urls.add("http://farm5.staticflickr.com/4869/46095816505_a2d2afa2eb.jpg")
        # urls.add("http://farm8.staticflickr.com/7879/46285664454_b7671ce936.jpg")
        # urls.add("http://farm5.staticflickr.com/4820/46095815965_b7ff236f06.jpg")
        # urls.add("http://farm8.staticflickr.com/7819/46095815685_5a7b873e5e.jpg")
        # urls.add("http://farm5.staticflickr.com/4854/46095815505_82ceea4879.jpg")
        # urls.add("http://farm8.staticflickr.com/7919/46095815325_1748585c8f.jpg")
        # urls.add("http://farm8.staticflickr.com/7828/46095815155_daebff737b.jpg")
        # urls.add("http://farm8.staticflickr.com/7859/46095814915_81856677b8.jpg")
        # urls.add("http://farm5.staticflickr.com/4866/46095814655_5848a89ac9.jpg")
        # urls.add("http://farm8.staticflickr.com/7883/40045097703_99aae8a41d.jpg")
        # urls.add("http://farm8.staticflickr.com/7871/46095814205_ff178d7497.jpg")
        # urls.add("http://farm5.staticflickr.com/4854/40045097323_24c9669296.jpg")
        # urls.add("http://farm5.staticflickr.com/4867/46095813805_b78ca9f51a.jpg")
        # urls.add("http://farm8.staticflickr.com/7822/40045096673_4bf669a6e7.jpg")
        # urls.add("http://farm5.staticflickr.com/4882/46095813305_063371fff3.jpg")
        # urls.add("http://farm5.staticflickr.com/4910/40045096033_5a79d8cb11.jpg")
        # urls.add("http://farm8.staticflickr.com/7906/46095812855_9d7a90daa8.jpg")
        # urls.add("http://farm5.staticflickr.com/4913/40045095673_16085c05d2.jpg")
        # urls.add("http://farm8.staticflickr.com/7903/46095812605_15cc4ca25b.jpg")
        # urls.add("http://farm5.staticflickr.com/4864/33134339858_306a051e26.jpg")

        request_url = "https://api-us.faceplusplus.com/facepp/v3/detect"

        api_key = "Mn2fDt_QekCPCyQaViVuwZ60E6jfzzXH"

        api_secret = "8OceY8JOsj8DWfc8PuDb6GZBbqdhhzZk"

        args = dict()

        args["api_key"] = api_key
        args["api_secret"] = api_secret

        args["return_attributes"] = "emotion"

        results = list()

        start_time = time()
        print(start_time)

        for url in urls:
            args["image_url"] = url
            response = requests.post(request_url, args)
            emotions = set()
            print(url)
            if response.status_code == 200:
                json_response = response.json()
                faces = json_response["faces"]
                for face in faces:
                    print(face["attributes"]["emotion"])
                    for emotion in face["attributes"]["emotion"]:
                        if face["attributes"]["emotion"][emotion] >= 50:
                            emotions.add(emotion)
                            break

            results.append((url, emotions))

        end_time = time()
        print(end_time)

        print(end_time - start_time)

        print(results)
