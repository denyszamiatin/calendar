todo = {}


def _append_task(date, task):
    if date not in todo:
        todo[date] = []
    todo[date].append(task)


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
