from rest_framework import serializers
from models import Cinemas as cinemas


class CinemasSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    image_url = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)
    detail_address = serializers.CharField(max_length=255)
    class Meta:
        model = cinemas
        fields = '__all__'

    def create(self, validated_data):
        return cinemas.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        cinemas.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass