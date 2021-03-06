from arango import ArangoClient


class PhotosInfoManager:

    def __init__(self):
        self.arangodb_client = ArangoClient(protocol='http', host='172.17.0.1', port=8529)
        self.arangodb = self.arangodb_client.db('int20h_test', username='root', password='secure')

        try:
            photos_info_collection = self.arangodb.create_collection('photos_info_collection')

            # Insert new documents into the collection.

            photos_info_collection.insert({"_key": "photos_info_document", "photos": []})
            photos_info_collection.insert({"_key": "last_update_date", "last_update": 0, "last_tag_update": 0})

        except:
            photos_info_collection = self.arangodb.collection('photos_info_collection')

            try:
                photos_info_collection.insert({"_key": "photos_info_document", "photos": []})
            except:
                pass

            try:
                photos_info_collection.insert({"_key": "last_update_date", "last_update": 0})
            except:
                pass


    def get_all_photos(self):
        photos_info_collection = self.arangodb.collection('photos_info_collection')
        photos_info_document = photos_info_collection.get("photos_info_document")
        return photos_info_document['photos']

    def push_photos_info(self, photos_info):
        if len(photos_info) == 0:
            return

        photos_info_collection = self.arangodb.collection('photos_info_collection')
        photos_info_document = photos_info_collection.get('photos_info_document')

        db_photos = photos_info_document['photos']

        for photo in photos_info:
            info_dict = dict()
            info_dict['url'] = photo[0]
            info_dict['emotions'] = list(photo[1])

            db_photos.append(info_dict)

        photos_info_document['photos'] = db_photos
        photos_info_collection.update(photos_info_document)

    def get_photo_urls(self):
        photos_info_collection = self.arangodb.collection('photos_info_collection')
        photos_info_document = photos_info_collection.get('photos_info_document')

        photo_urls = set()
        for photo in photos_info_document['photos']:
            photo_urls.add(photo['url'])

        return photo_urls

    def update_album_update_date(self, new_date):
        photos_info_collection = self.arangodb.collection('photos_info_collection')
        update_date_document = photos_info_collection.get("last_update_date")
        update_date_document['last_update'] = new_date
        photos_info_collection.update(update_date_document)

    def update_tag_update_date(self, new_date):
        photos_info_collection = self.arangodb.collection('photos_info_collection')
        update_date_document = photos_info_collection.get("last_update_date")
        update_date_document['last_tag_update'] = new_date
        photos_info_collection.update(update_date_document)

    def get_album_update_date(self):
        photos_info_collection = self.arangodb.collection('photos_info_collection')
        try:
            photos_info_collection.insert({"_key": "last_update_date", "last_update": 0})
        except:
            print("date doc exists")

        update_date_document = photos_info_collection.get("last_update_date")
        return update_date_document['last_update']

    def get_tag_update_date(self):
        photos_info_collection = self.arangodb.collection('photos_info_collection')
        update_date_document = photos_info_collection.get("last_update_date")
        try:
            return update_date_document['last_tag_update']
        except:
            print("last_tag_update key not yet created")
        return 0



photos_info_db_manager = PhotosInfoManager()
