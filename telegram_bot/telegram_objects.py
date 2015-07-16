from jsonobject import *


class Message(JsonObject):
    text = StringProperty()


class Update(JsonObject):
    update_id = IntegerProperty(required=True)
    message = ObjectProperty(Message)
