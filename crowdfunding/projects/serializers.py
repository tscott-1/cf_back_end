from rest_framework import serializers
from django.apps import apps
from users.serializers import CustomUserSerializer
from users.models import CustomUser


class PledgeSerializer(serializers.ModelSerializer):

    supporter = CustomUserSerializer(many = False, read_only=True)
    class Meta:
        model = apps.get_model('projects.Pledge')
        fields = '__all__'




class SportsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = apps.get_model('projects.SportsList')
        fields = '__all__'


class ClubsSerializer(serializers.ModelSerializer):
    club_owner = CustomUserSerializer(many = False, read_only=True)
    members = CustomUserSerializer(source = 'club_members', many=True, read_only=True)
    sport = SportsSerializer(many=False, read_only=True)
    class Meta:
        model = apps.get_model('projects.Sportsclub')
        fields = ('id', 'club_owner', 'club', 'description', 'club_size', 'club_location', 'is_active', 'club_logo', 'sport', 'club_members', 'members')
        exta_kwargs = {'club_members': {'required': False}}

class ProjectSerializer(serializers.ModelSerializer):
    # TODO make enddate date_created + 30 by default
    pledges = PledgeSerializer(many=True, read_only=True)
    club = ClubsSerializer(source = 'owner_club', many = False, read_only=True)
    class Meta:
        model = apps.get_model('projects.Project')
        fields = ('id', 'title', 'description', 'goal', 'image', 'fund_type', 'is_open', 'date_created', 'end_date', 'member_only', 'club','owner_club', 'pledges')



class ProjectDetailSerializer(ProjectSerializer):
    # pledges = PledgeSerializer(many=True, read_only=True)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.fund_type = validated_data.get('fund_type', instance.fund_type)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.end_date = validated_data.get('date_created', instance.date_created)
        instance.owner_club = validated_data.get('owner_club', instance.owner_club)
        instance.save()
        return instance

class PledgeDetailSerializer(PledgeSerializer):
    project = ProjectDetailSerializer(many=False,read_only=True )
    
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
        instance.save()
        # instance.club_members.set(validated_data.get("club_members"))
        list = instance.club_members.all()
        new_list =[]
        for member_id in validated_data.get("club_members", instance.club_members):
            # member = CustomUser.objects.get(id=member_id)     
            if member_id not in new_list:
                new_list.append(member_id)
        for member_id in list:
            if member_id not in new_list:
                new_list.append(member_id)
        instance.club_members.set(new_list)
        return instance
    
    
class SportDetailSerializer(SportsSerializer):
 
    def update(self,instance, validated_data):
        instance.sport = validated_data.get('sport', instance.sport)
        instance.sport_type = validated_data.get('sport_type', instance.sport_type)
        instance.save()
        return instance
