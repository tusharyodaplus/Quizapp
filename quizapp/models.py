from django.db import models

from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Quiz(models.Model):
    category =models.CharField(max_length = 250)
    description=models.CharField(max_length = 250)
    def __str__(self):
        return self.category

class QuizTaker(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score= models.IntegerField(default=0)
    def __str__(self):
        return str(self.user)    'naj599vd8g489goin9u6ytfbme54pups'

class Question(models.Model):
    CAT_CHOICES = (
    ('sports','Sports'),
    ('movies','Movies'),
    ('maths','Maths'),
    ('generalknowledge','GeneralKnowledge')
    )
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
     
    question = models.CharField(max_length = 250)
    optiona = models.CharField(max_length = 100)
    optionb = models.CharField(max_length = 100)
    optionc = models.CharField(max_length = 100)
    optiond = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    category = models.CharField(max_length=20, choices = CAT_CHOICES)

    class Meta:
        ordering = ('-category',)
    def __str__(self):
        return self.question

class UserTracker(models.Model):
        question = models.ForeignKey(Question,on_delete=models.CASCADE)
        
        user = models.ForeignKey(User,on_delete=models.CASCADE)
        result= models.CharField(max_length = 250)
        user_answer= models.CharField(max_length = 250)
        correct_or_incorrect = models.CharField(max_length = 100)
        def __str__(self):
            return self.user_answer


class AccountData(models.Model):
    quiztaker = models.ForeignKey(QuizTaker,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    
    key = models.CharField(max_length=30)
    value = models.CharField(max_length=30, null=True, blank=True)
    def __str__(self):
            return self.key
    
    
    
     


        




