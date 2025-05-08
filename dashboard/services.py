class TaskService:
    def __init__(self, user):
        self.user = user

    def get_tasks_for_user(self):
        return Task.objects.filter(assigned_to=self.user)

    def count_by_status(self, status):
        return Task.objects.filter(assigned_to=self.user, status=status).count()
