from flask import Flask

from app.conf.config import Config


try:
    app = Flask(__name__)
    app.config.from_object(Config)

    from app import routes

    if __name__ == '__main__':
        app.run(debug=True)


except Exception as e:
    exit(-4)
