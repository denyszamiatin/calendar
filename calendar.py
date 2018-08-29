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