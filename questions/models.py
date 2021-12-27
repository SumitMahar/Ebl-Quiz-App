from django.db import models

from quizes.models import Quiz

class Question(models.Model):
    question_text = models.TextField()
    marks = models.IntegerField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.question_text[:20]}..."
    
    def get_answers(self):
        return self.answer_set.all() 


class Answer(models.Model):
    answer_text = models.CharField(max_length=250)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"question: {self.question.question_text[:10]}, answer: {self.answer_text[:10]}, correct: {self.is_correct}"
