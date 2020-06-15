from django.contrib import admin
from .models import Questions,Quiz,QuizTakers

# Register your models here.
admin.site.register(Questions)
admin.site.register(Quiz)
admin.site.register(QuizTakers)

