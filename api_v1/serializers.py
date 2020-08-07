from rest_framework.utils.serializer_helpers import ReturnDict

from user.models import CustomUser, Activity
from rest_framework import serializers
from django.utils import timezone


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ["start_time", "end_time"]


class UserActivitySerializer(serializers.ModelSerializer):
    real_name = serializers.SerializerMethodField()
    activity_periods = ActivitySerializer(many=True, read_only=True)
    tz = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ["id", "real_name","tz", "activity_periods"]

    def get_real_name(self, obj):
        real_name = obj.first_name + " " + obj.last_name
        return real_name

    def get_tz(self, obj):
        return timezone.now().tzinfo.__str__()

