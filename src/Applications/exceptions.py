class NoApplicationExist(Exception):
    def __init__(self, name: str):
        self.name = name


class NoConnectionWithRedis(Exception):
    def __init__(self, name: str):
        self.name = name
