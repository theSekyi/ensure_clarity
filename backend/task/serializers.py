from rest_framework import serializers
from .models import Task,SubTask


class SubTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubTask
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    main_task = SubTaskSerializer(many=True)

    class Meta:
        model = Task
        fields = '__all__'


