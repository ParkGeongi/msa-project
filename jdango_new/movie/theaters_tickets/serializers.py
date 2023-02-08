from rest_framework import serializers
from models import Theater_ticket as theater_ticket

class Theater_ticketSerializer(serializers.ModelSerializer):
    class Meta:
        model = theater_ticket
        fields = '__all__'

    def create(self, validated_data):
        return theater_ticket.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        theater_ticket.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass