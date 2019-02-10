from arango import ArangoClient


class PhotosInfoManager:

    def __init__(self):
        self.arangodb_client = ArangoClient(protocol='http', host='172.17.0.1', port=8529)
        self.arangodb = self.arangodb_client.db('int20h_test', username='root', password='secure')

        try:
            photos_info_collection = self.arangodb.create_collection('photos_info_collection')

            # Insert new documents into the collection.
            photos_info_collection.insert({'_key': 'photos_info_document', 'photos': []})

        except:
            pass

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


photos_info_db_manager = PhotosInfoManager()
