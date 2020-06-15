from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):
    
    category=models.CharField(max_length = 250)
    description=models.CharField(max_length = 250)
    

    def __str__(self):
        return self.category
    
     

class QuizTakers(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score= models.CharField(max_length = 250)
    def __str__(self):
        return self.user

class Questions(models.Model):
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
    catagory = models.CharField(max_length=20, choices = CAT_CHOICES)

    class Meta:
        ordering = ('-catagory',)

    def __str__(self):
        return self.question