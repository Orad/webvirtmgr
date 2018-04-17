from rest_framework import serializers

from instance.models import RunningHistory


# serializer class for Running History model
class RunningHistorySerializer(serializers.ModelSerializer):
	
    class Meta:
        model = RunningHistory
        fields = ('instance', 'event')
        