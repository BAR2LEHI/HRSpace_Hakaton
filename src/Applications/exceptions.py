class NoApplicationExist(Exception):
    def __init__(self, id: int):
        self.id = id


class NoApplicationsExist(Exception):
    pass
