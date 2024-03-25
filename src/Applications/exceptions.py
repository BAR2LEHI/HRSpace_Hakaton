<<<<<<< HEAD
class NoApplicationExist(Exception):
    def __init__(self, name: str):
        self.name = name
=======
class NoApplicationExist(Exception):
    def __init__(self, name: str):
        self.name = name


class NoConnectionWithRedis(Exception):
    def __init__(self, name: str):
        self.name = name
>>>>>>> cdb9752fd6b1e226e5daead3c7a00011e892c264
