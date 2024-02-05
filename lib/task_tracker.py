class Task_tracker():
    def __init__(self):
        self.tasks_list = []
    
    def add(self, task):
        self.tasks_list.append(task)

    def complete(self, task):
        self.tasks_list.remove(task)