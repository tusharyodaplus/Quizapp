from django.db import models

# Create your models here.

class Questions(models.Model):
    CAT_CHOICES = (
    ('sports','Sports'),
     ('maths','Maths'))
    
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
