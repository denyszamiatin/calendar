import pickle
import configparser


config = configparser.ConfigParser()
config.read('calendar.ini')


FILENAME = config['Serializer']['Filename']


def load_tasks(filename=FILENAME):
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}


def save_tasks(obj, filename=FILENAME):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)


def _append_task(date, task):
    if date not in todo:
        todo[date] = []
    todo[date].append(task)
    save_tasks(todo)


def _list_tasks(date):
    if date not in todo:
        raise ValueError
    return tuple(todo[date])


def append_task():
    date = input('Date?')
    task = input('Task?')
    _append_task(date, task)


def list_tasks():
    date = input('Date?')
    try:
        for task in _list_tasks(date):
            print(task)
    except ValueError:
        print('There are no tasks on this day')


todo = load_tasks()

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
