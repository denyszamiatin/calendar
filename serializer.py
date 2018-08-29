import abc


class Serializer(metaclass=abc.ABCMeta):
    EXTENSION = ''

    def __init__(self, filename):
        self.filename = filename + self.EXTENSION

    @abc.abstractmethod
    def _load(self):
        pass

    def load(self):
        try:
            return self._load()
        except FileNotFoundError:
            return {}