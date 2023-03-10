from rest_framework import serializers
from .models import Product as product

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    price = serializers.CharField()
    image_url = serializers.CharField()

    class Meta:
        model = product
        fields = '__all__'

    def create(self, validated_data):
        return product.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        product.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self,instance, valicated_data):
        pass
