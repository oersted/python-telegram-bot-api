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

    def update(self, limit=None, timeout=None):
        options = {}
        if limit is not None:
            options['limit'] = limit
        if timeout is not None:
            options['timeout'] = timeout
        if self.next_update is not None:
            options['offset'] = self.next_update

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

    def send_message(self, chat, text, keyboard=None):
        options = {'chat_id': chat.id, 'text': text}
        if keyboard:
            options['reply_markup'] = keyboard.to_json()

        self._request('sendMessage', options)

    def _request(self, method, options={}):
        json_response = get(self.URL.format(token=self.token, method=method), params=options).text

        if json_response:
            response = loads(json_response)

            if response['ok']:
                return response['result']
            else:
                raise FailedTelegramResponse(response['error_code'])
