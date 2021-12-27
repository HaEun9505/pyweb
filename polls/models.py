from django.db import models

# Question 모델(Model을 상속받음)- 테이블과 같은 의미
class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.question_text

#Choice 모델
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text