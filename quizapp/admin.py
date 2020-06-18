from django.contrib import admin
from .models import Questions,Quiz,QuizTakers,UserTracker

# Register your models here.
admin.site.register(Questions)
admin.site.register(Quiz)
admin.site.register(QuizTakers)
admin.site.register(UserTracker)

