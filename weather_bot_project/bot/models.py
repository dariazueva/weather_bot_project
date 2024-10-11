from django.db import models


class Log(models.Model):
    user_id = models.BigIntegerField()
    command = models.CharField(max_length=255)
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User {self.user_id} - {self.command} at {self.timestamp}"
