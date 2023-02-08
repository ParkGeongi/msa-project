from rest_framework import serializers
from .models import SeqUser as sequser

class SeqUserSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField()
    password = serializers.CharField()
    user_name = serializers.CharField()
    phone = serializers.CharField()
    birth = serializers.CharField()
    address = serializers.CharField()
    job = serializers.CharField()
    user_interests = serializers.CharField()
    token = serializers.CharField()
    class Meta:
        model = sequser
        fields = '__all__'

    def create(self,validated_data):
        return sequser.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        sequser.objects.filter(pk=instance.id).update(**valicated_data)


    def delete(self, instance, valicated_data):
        pass