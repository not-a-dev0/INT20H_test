from arango import ArangoClient


class PhotosInfoManager:

    def __init__(self):
        self.arangodb_client = ArangoClient(protocol='http', host='localhost', port=8529)
        self.arangodb = self.arangodb_client.db('int20h_test', username='int20h_test_user', password='int20h')

        try:
            photos_info_collection = self.arangodb.create_collection('photos_info_collection')

            # Insert new documents into the collection.
            photos_info_collection.insert({"photos": []})

        except:
            print("collection already exists")

    def get_all_photos(self):
        photos_info_collection = self.arangodb.collection('photos_info_collection')
        photos_info_document = photos_info_collection.get("photos_info_document")
        return photos_info_document['photos']

    def push_photos_info(self, photos_info):
        if len(photos_info) == 0:
            return

        print("\n\npush photos info:")
        photos_info_collection = self.arangodb.collection('photos_info_collection')
        photos_info_document = photos_info_collection.get("photos_info_document")

        print("input photos_info:")
        print(photos_info)

        db_photos = photos_info_document['photos']
        print("\ndb_photos")
        print(db_photos)

        # # additional check for escaping duplications - make set
        # # from db photo urls (but we already did it in db_updater)

        # db_photo_urls_set = set()
        # for photo in db_photos:
        #     db_photo_urls_set.add(photo['url'])
        #
        # input_photo_urls_set = set()
        # for photo in photos_info:
        #     input_photo_urls_set.add(photo[0])
        #
        # print("\n\ndb_photo_urls_set:")
        # print(db_photo_urls_set)
        #
        # print("\n\ninput_photo_urls_set:")
        # print(input_photo_urls_set)
        #
        # photo_urls_to_add = input_photo_urls_set.difference(db_photo_urls_set)
        #
        # print("\nphoto_urls_to_add")
        # print(photo_urls_to_add)

        print("\n\nnew photos info to push:")
        for photo in photos_info:
            info_dict = dict()
            info_dict['url'] = photo[0]
            info_dict['emotions'] = list(photo[1])

            print(info_dict)

            db_photos.append(info_dict)

        print("\npushing new photos' info to db")
        photos_info_document['photos'] = db_photos
        photos_info_collection.update(photos_info_document)

    def get_photo_urls(self):
        photos_info_collection = self.arangodb.collection('photos_info_collection')
        photos_info_document = photos_info_collection.get("photos_info_document")

        photo_urls = set()
        for photo in photos_info_document['photos']:
            photo_urls.add(photo['url'])

        return photo_urls


photos_info_db_manager = PhotosInfoManager()
