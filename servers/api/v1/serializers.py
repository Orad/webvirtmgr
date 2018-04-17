from rest_framework import serializers

from servers.models import Compute


class ComputeSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = Compute
        fields = ('id','name','hostname','login','password','type','organization')
    