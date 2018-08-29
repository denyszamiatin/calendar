import pickle
import json
import configparser
import abc


config = configparser.ConfigParser()
config.read('calendar.ini')

FILENAME = config['Serializer']['Filename']


class Serializer(metaclass=abc.ABCMeta):
    EXTENSION = ''

    def __init__(self, filename=FILENAME):
        self.filename = filename + self.EXTENSION

    @abc.abstractmethod
    def _load(self):
        pass

    def load(self):
        try:
            return self._load()
        except FileNotFoundError:
            return {}


class PickleSerializer(Serializer):
    EXTENSION = '.pickle'

    def _load(self):
        with open(self.filename, 'rb') as f:
            return pickle.load(f)

    def save(self, obj):
        with open(self.filename, 'wb') as f:
            pickle.dump(obj, f)


class JsonSerializer(Serializer):
    EXTENSION = '.json'

    def _load(self):
        with open(self.filename, 'rt') as f:
            return json.load(f)

    def save(self, obj):
        with open(self.filename, 'wt') as f:
            json.dump(obj, f)


class Calendar:
    def __init__(self, serializer):
        self.serializer = serializer
        self.todo = self.serializer.load()

    def append(self, date, task):
        if date not in self.todo:
            self.todo[date] = []
        self.todo[date].append(task)
        self.serializer.save(self.todo)

    def list(self, date):
        if date not in self.todo:
            raise ValueError
        return tuple(self.todo[date])


if config['Serializer']['Type'] == 'JSON':
    serializer = JsonSerializer()
elif config['Serializer']['Type'] == 'Pickle':
    serializer = PickleSerializer()
else:
    raise TypeError

calendar = Calendar(serializer)


def append_task():
    date = input('Date?')
    task = input('Task?')
    calendar.append(date, task)


def list_tasks():
    date = input('Date?')
    try:
        for task in calendar.list(date):
            print(task)
    except ValueError:
        print('There are no tasks on this day')


while True:
    print("""a - append task
l - list tasks
q - quit""")
    action = input('?').lower()
    if action == 'a':
        append_task()
    elif action == 'l':
        list_tasks()
    elif action == 'q':
        break
