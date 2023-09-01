from django.forms import model_to_dict
from rest_framework import serializers

from .models import Topic, Content

import sys
sys.path.append("..")

from courses.serializers import UnitSerializer


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        unit = UnitSerializer()
        # fields = "__all__"
        fields = ["id", "topic_code", "name", "period", "unit"]

    # def update(self, instance, validated_data):
    #     instance.topic_code = validated_data.get("topic_code", instance.topic_code)
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.years = validated_data.get("years", instance.years)
    #     instance.sem_count = validated_data.get("sem_count", instance.sem_count)
    #
    #     instance.save()
    #     return instance




class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"
        topic = TopicSerializer()
        # fields = ["id", "name", "topic", "description"]

    # def update(self, instance, validated_data):
    #     instance.topic_code = validated_data.get("topic_code", instance.topic_code)
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.years = validated_data.get("years", instance.years)
    #     instance.sem_count = validated_data.get("sem_count", instance.sem_count)
    #
    #     instance.save()
    #     return instance



