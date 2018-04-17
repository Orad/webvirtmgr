from rest_framework import serializers

from instance.models import RunningHistory


# serializer class for Running History model
class RunningHistorySerializer(serializers.ModelSerializer):
    instance_name = serializers.CharField()

    class Meta:
        model = RunningHistory
        fields = ('instance_name', 'event')
        