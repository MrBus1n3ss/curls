from datetime import datetime


class Request:

    def __init__(self, name, verb):
        self.name = name
        self.verb = verb
        self.created_at = datetime.now()

