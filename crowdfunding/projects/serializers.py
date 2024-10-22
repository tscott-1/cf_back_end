from rest_framework import serializers
from django.apps import apps

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')
    class Meta:
        model = apps.get_model('projects.Pledge')
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    class Meta:
        model = apps.get_model('projects.Project')
        fields = '__all__'

class ClubsSerializer(serializers.ModelSerializer):
    club_owner = serializers.ReadOnlyField(source='club_owner.id')
    class Meta:
        model = apps.get_model('projects.Sportsclub')
        fields = '__all__'

class SportsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = apps.get_model('projects.SportsList')
        fields = '__all__'


class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

class PledgeDetailSerializer(PledgeSerializer):
    # project = ProjectDetailSerializer(many=False,read_only=True )

    def update(self,instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get('anoynymous', instance.anonymous)
        instance.project = validated_data.get('project', instance.project)
        instance.supporter = validated_data.get('supporter', instance.supporter)
        instance.save()
        return instance
    
class ClubDetailSerializer(ClubsSerializer):
 
    def update(self,instance, validated_data):
        instance.club = validated_data.get('club', instance.club)
        instance.sport = validated_data.get('sport', instance.sport)
        instance.club_size = validated_data.get('club_size', instance.club_size)
        instance.club_location = validated_data.get('club_location', instance.club_location)
        instance.club_logo = validated_data.get('club_logo', instance.club_logo)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.club_owner = validated_data.get('club_owner', instance.club_owner)
        instance.club_members = validated_data.get('club_members', instance.club_members)
        instance.save()
        return instance
    
    
class SportDetailSerializer(SportsSerializer):
 
    def update(self,instance, validated_data):
        instance.sport = validated_data.get('sport', instance.sport)
        instance.sport_type = validated_data.get('sport_type', instance.sport_type)
        instance.save()
        return instance
