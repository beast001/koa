from rest_framework import serializers

class PointSerializer(serializers.Serializer):
    id=serializers.IntegerField(label="Enter unique Id")
    points = serializers.CharField(label="Enter points")
    
