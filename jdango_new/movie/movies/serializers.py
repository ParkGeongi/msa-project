from rest_framework import serializers
from models import Movies as movies

class MoviesSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    director = serializers.CharField()
    description = serializers.CharField()
    poster_url = serializers.CharField()
    running_time = serializers.CharField()
    age_rating = serializers.CharField()
    class Meta:
        model = movies
        fields = '__all__'

    def create(self,validated_data):
        return movies.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        movies.objects.filter(pk=instance.id).update(**valicated_data)


    def delete(self, instance, valicated_data):
        pass