from mongoengine import *

def connect_db():
    # connect(db = 'userdata', host = 'db', port = 5000, username = 'sreejon', password = '12345')

    connect(db = 'userdata', host = 'db', port = 5000)

    # connect(db = 'userdata', host = 'db', port = 27017)

    # connect( db = 'userdata', host = 'localhost', port = 27017 )