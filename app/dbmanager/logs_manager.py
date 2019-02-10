import logging.handlers

import datetime

from arango import ArangoClient


class Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance


class ArangoLogHandler(Singleton, logging.Handler):
    """
    Logging handler for ArangoDB.

    """

    def __init__(self):
        super().__init__()
        self.arangodb_client = ArangoClient(protocol='http', host='172.17.0.1', port=8529)
        self.arangodb = self.arangodb_client.db('int20h_test', username='root', password='secure')

        try:
            self.arangodb.create_collection('logs')
        except:
            pass

        self.logs_collection = self.arangodb.collection('logs')

    def emit(self, record):
        msg = str(record.__dict__['msg'])
        if len(record.__dict__['args']) > 0:
            msg += '; args: ' + str(record.__dict__['args'])
        if record.__dict__['exc_info'] is not None:
            msg += str(record.__dict__['exc_info']) + str(record.__dict__['exc_text']) + str(
                record.__dict__['stack_info'])

        log = {
            '_key': str(datetime.datetime.now()).replace(' ', '_'),
            'pathname': record.__dict__['pathname'],
            'level': record.__dict__['levelname'],
            'func_name': record.__dict__['funcName'],
            'line_no': record.__dict__['lineno'],
            'msg': msg
        }

        self.logs_collection.insert(log)
