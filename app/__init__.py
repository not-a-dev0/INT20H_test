from flask import Flask
from app.threads.DB_updater import DBUpdater
from app.conf.config import Config

try:
    app = Flask(__name__)
    app.config.from_object(Config)

    from app import routes

    db_updater = DBUpdater("Database Updater")
    db_updater.start()

    if __name__ == '__main__':
        app.run(debug=True)


except Exception as e:
    exit(-4)
