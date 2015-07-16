from jsonobject import *
from json import dumps


class Keyboard:
    def __init__(self, matrix, one_time=None):
        self.matrix = matrix
        self.one_time = one_time

    def to_json(self):
        json = '"keyboard": {}'.format(dumps(self.matrix))
        if self.one_time is not None:
            json += ', "one_time_keyboard": {}'.format(dumps(self.one_time))
        json = '{' + json + '}'
        return json


class Chat(JsonObject):
    id = IntegerProperty()


class Message(JsonObject):
    text = StringProperty()
    chat = ObjectProperty(Chat)


class Update(JsonObject):
    update_id = IntegerProperty(required=True)
    message = ObjectProperty(Message)
