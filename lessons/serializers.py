from rest_framework import serializers
from .models import Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['id', 'student', 'category', 'place', 'date_time', 'created']
        # Todo serialize student without be default