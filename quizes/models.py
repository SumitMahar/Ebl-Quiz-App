from django.db import models
import random

DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard')
)
class Quiz(models.Model):
    name = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    no_of_questions = models.IntegerField()
    duration = models.IntegerField(help_text="Duration of the Quiz in minutes")
    req_score_to_pass = models.IntegerField(help_text="Required score in %")
    difficulty = models.CharField(max_length=20, choices=DIFF_CHOICES)

    def __str__(self) -> str:
        return f"{self.name} - {self.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.no_of_questions]

    class Meta:
        verbose_name_plural = "Quizes"