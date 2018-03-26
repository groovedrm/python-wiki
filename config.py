import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SECRET_PASSPHRASE_CCRF'
    MAPRISK_KEY = os.environ.get(
        'MAPRISK_KEY') or 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI1YWI1NWNkOTY1MTA3MDAxYmM0ZmVhZmEiLCJleHAiOm51bGx9.LURAjucAQ269BzsxWcUp2PysqCZBNOam8oA39fjV-m4'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
