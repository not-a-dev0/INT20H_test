import os


class Config(object):
    # SECRET_KEY = os.environ.get('SECRET_KEY')

    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
