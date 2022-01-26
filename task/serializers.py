from rest_framework import serializers
from .models import Task,SubTask


class SubTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubTask
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    main_task = SubTaskSerializer(many=True)

    def create(self, validated_data):
        temp_task_details = validated_data.pop('sub_task')
        new_task = Task.objects.create(**validated_data)
        for i in temp_task_details:
            SubTaskSerializer.objects.create(**i, task=new_task)
        return new_task


    class Meta:
        model = Task
        fields = '__all__'


