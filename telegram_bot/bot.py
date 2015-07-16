from requests import get
from json import loads
from Queue import Queue

from exceptions import FailedTelegramResponse
from telegram_objects import Update


class TelegramBot:
    URL = "https://api.telegram.org/bot{token}/{method}"

    def __init__(self, token):
        self.token = token
        self.next_update = None
        self.updates = Queue()

    def update(self):
        options = {}
        if self.next_update:
            options = {'offset': self.next_update}

        for json_update in self._request('getUpdates', options):
            update = Update(json_update)
            if self.next_update is None:
                self.next_update = update.update_id
            elif update.update_id == self.next_update:
                self.updates.put(update)
                self.next_update += 1
            else:
                break

    def has_next(self):
        return not self.updates.empty()

    def next(self):
        return self.updates.get().message

    def _request(self, method, options={}):
        json_response = get(self.URL.format(token=self.token, method=method), params=options).text

        if json_response:
            response = loads(json_response)

            if response['ok']:
                return response['result']
            else:
                raise FailedTelegramResponse(response['error_code'])