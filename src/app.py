# TaskManager Pro - Aplicación principal
class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        return True

if __name__ == "__main__":
    manager = TaskManager()
    print("TaskManager Pro v1.0.0")
