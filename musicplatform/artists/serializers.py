from rest_framework import serializers
from .models import Artist


class ArtistSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    stage_name = serializers.CharField(max_length=255)
    social_link = serializers.URLField(max_length=255)

    def create(self, validated_data):
        return Artist.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.stage_name = validated_data.get('stage_name', instance.stage_name)
        instance.social_link = validated_data.get('social_link', instance.social_link)
        instance.save()
        return instance