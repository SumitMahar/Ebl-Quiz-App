from django.db import models
from django.contrib.auth.models import User

from accounts.models import CustomUser

from quizes.models import Quiz

class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    attempts = models.IntegerField()
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quiz: {self.quiz}, User: {self.user}, Score: {self.score}"
