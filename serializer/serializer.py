import abc

__all__ = ('get_serializer',)


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


def get_serializer(type_, filename):
    if type_ == 'JSON':
        from . import json_serializer
        return json_serializer.JsonSerializer(filename=filename)
    elif type_ == 'Pickle':
        from . import pickle_serializer
        return pickle_serializer.PickleSerializer(filename=filename)
    else:
        raise TypeError