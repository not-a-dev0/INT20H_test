from flask import Flask

import logging.config
import yaml
from os import path, makedirs

from app.threads.DB_updater import DBUpdater
from app.conf.config import Config

try:
    app = Flask(__name__)
    app.config.from_object(Config)

    if not path.exists('logs'):
        makedirs('logs')
        logs_file = open('logs/logs.log', 'x')
        logs_file.close()

    if not path.exists('logs/logs.log'):
        logs_file = open('logs/logs.log', 'x')
        logs_file.close()

    with open('app/conf/logging.yml', 'r') as stream:
        logging_config = yaml.load(stream)
    logging.config.dictConfig(logging_config)

    from app.dbmanager.logs_manager import ArangoLogHandler
    app.logger.addHandler(ArangoLogHandler())

    logger = logging.getLogger('logger')

    # example of using logger
    # logger.debug('debug message')
    # logger.info('info message')
    # logger.warning('warning message')
    # logger.error('error message')
    # logger.critical('critical message')

    # example of using logger with exceptions
    # try:
    #     open('/path/to/does/not/exist', 'rb')
    # except (SystemExit, KeyboardInterrupt):
    #     raise
    # except Exception as e:
    #     logger.error('Failed to open file', exc_info=True)

    from app import routes

    db_updater = DBUpdater('Database Updater')
    db_updater.start()

    if __name__ == '__main__':
        app.run(debug=True)


except Exception as e:
    exit(-4)
