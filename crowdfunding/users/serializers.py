from rest_framework import serializers
from .models import CustomUser
# from projects.serializers import ClubsSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    # clubs = serializers.ReadOnlyField(source='sportsclub.id', many=True)
    
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)