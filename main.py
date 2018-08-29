import configparser
import calendar as cal_mod
import serializer

config = configparser.ConfigParser()
config.read('calendar.ini')

FILENAME = config['Serializer']['Filename']

calendar = cal_mod.Calendar(serializer.get_serializer(config['Serializer']['Type'], FILENAME))


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
