from jsonobject import *


class Chat(JsonObject):
    id = IntegerProperty()


class Message(JsonObject):
    text = StringProperty()
    chat = ObjectProperty(Chat)


class Update(JsonObject):
    update_id = IntegerProperty(required=True)
    message = ObjectProperty(Message)
