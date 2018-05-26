from mongoengine import *
import datetime

class users(Document):
    created = DateTimeField(default = datetime.datetime.utcnow)
    userId = IntField(min_value = 1)
    fullName = StringField(max_length = 100)
    firstName = StringField(max_length = 50)
    lastName = StringField(max_length = 50)
    password = StringField(max_length = 30)
    tags = ListField(StringField(max_length = 30))

    expiry = IntField(min_value = 1)

    meta = {
        'strict': False,
        'ordering': ['-created'],
        'indexes': [
            {
                'fields': ['expiry'],
                'expireAfterSeconds': 5
            }
        ]
    }