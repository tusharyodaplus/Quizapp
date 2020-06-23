
from .models import Quiz
from rest_framework import serializers

class quizSerializer(serializers.ModelSerializer):
	class Meta:
		model = Quiz
		fields =('category','description')
	