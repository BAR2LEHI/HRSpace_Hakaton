<<<<<<< HEAD
# Кастомные исключения
=======
class NoApplicationExist(Exception):
    def __init__(self, id: int):
        self.id = id


class NoApplicationsExist(Exception):
    pass
>>>>>>> dcbd0231447a19e42e108c0744af24682a7509d7
