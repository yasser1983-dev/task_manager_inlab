from .forms import TaskForm

def get_task_form(*args, **kwargs):
    return TaskForm(*args, **kwargs)


from .services import TaskService

class TaskServiceFactory:
    @staticmethod
    def create(user):
        return TaskService(user)
