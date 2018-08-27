todo = {}

while True:
    print("""a - append task
l - list tasks
q - quit""")
    action = input('?').lower()
    if action == 'a':
        date = input('Date?')
        task = input('Task?')
        if date not in todo:
            todo[date] = []
        todo[date].append(task)
    elif action == 'l':
        date = input('Date?')
        if date not in todo:
            print('There are no tasks on this day')
        else:
            print(date)
            for task in todo[date]:
                print(task)
    elif action == 'q':
        break
