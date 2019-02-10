from arango import ArangoClient


class DBInitializer:

    @staticmethod
    def init_db():
        arangodb_client = ArangoClient(protocol='http', host='172.17.0.1', port=8529)

        sys_db = arangodb_client.db('_system', username='root', password='secure')
        try:
            sys_db.create_database('int20h_test')
        except:
            pass
