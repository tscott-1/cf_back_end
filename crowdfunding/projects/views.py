from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404
from .models import Project, Pledge, Sportsclub, SportsList
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer, PledgeDetailSerializer, SportsSerializer, SportDetailSerializer, ClubsSerializer, ClubDetailSerializer
from .permissions import IsOwnerOrReadOnly, IsSuppporterOrReadOnly, IsClubMemberOrReadOnly, IsClubOwnerOrReadOnly

class ProjectList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly
        ]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
  
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            # club_id = project.get('owner_club')
            # owner = Project.owner_club.get('club_owner')
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)
    
    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(
            instance=project,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(
            {"detail": "PRoject successfully deleted"},
            status=status.HTTP_204_NO_CONTENT
        )


class PledgeList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class PledgeDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsSuppporterOrReadOnly
    ]

    def get_object(self, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except pledge.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        Pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(Pledge)
        return Response(serializer.data)
    
    def put(self, request, pk):
        Pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(
            instance=Pledge,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request, pk):
        pledge = self.get_object(pk)
        pledge.delete()
        return Response(
             {"detail": "Pledge successfully deleted"},
            status=status.HTTP_204_NO_CONTENT
        )
    

class SportList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        sports = SportsList.objects.all()
        serializer = SportsSerializer(sports, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SportDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class SportDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        permissions.IsAdminUser,
    ]

    def get_object(self, pk):
        try:
            sport = SportsList.objects.get(pk=pk)
            self.check_object_permissions(self.request, sport)
            return sport
        except sport.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        sport = self.get_object(pk)
        serializer = SportDetailSerializer(sport)
        return Response(serializer.data)
    
    def put(self, request, pk):
        sport = self.get_object(pk)
        serializer = SportDetailSerializer(
            instance=sport,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class Clublist(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        clubs = Sportsclub.objects.all()
        serializer = ClubsSerializer(clubs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClubsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(club_owner=request.user, club_members = [request.user])
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class ClubDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsClubOwnerOrReadOnly,
    ]

    def get_object(self, pk):
        try:
            club = Sportsclub.objects.get(pk=pk)
            self.check_object_permissions(self.request, club)
            return club
        except club.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        club = self.get_object(pk)
        serializer = ClubDetailSerializer(club)
        return Response(serializer.data)
    
    def put(self, request, pk):
        club = self.get_object(pk)
        serializer = ClubDetailSerializer(
            instance=club,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request, pk):
        club = self.get_object(pk)
        club.delete()
        return Response(
            {"detail": "Club successfully deleted"},
            status=status.HTTP_204_NO_CONTENT
        )
    