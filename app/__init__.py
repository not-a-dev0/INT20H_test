from flask import Flask

import logging.config
import yaml
from os import path, makedirs

from app.conf.config import Config

from app.dbmanager.logs_manager import ArangoLogHandler
from app.dbmanager.db_initializer import DBInitializer

from app.db_updater.DB_updater import DBUpdater

DBInitializer.init_db()

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

logger = logging.getLogger('logger')

try:
    app = Flask(__name__)
    app.config.from_object(Config)

    app.logger.addHandler(ArangoLogHandler())

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


except Exception as e:
    logger.warning(e)
