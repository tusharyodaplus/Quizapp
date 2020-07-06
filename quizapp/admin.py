from django.contrib import admin
from .models import Question,Quiz,QuizTaker,UserTracker,AccountData

# Register your models here.
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(QuizTaker)
admin.site.register(UserTracker)
admin.site.register(AccountData)

