# comments when i feel like it

from django.urls import path
from . import views

urlpatterns = [
  path('projects/', views.ProjectList.as_view()),
  path('projects/<int:pk>/', views.ProjectDetail.as_view()),
  path('pledges/', views.PledgeList.as_view()),
  path('pledges/<int:pk>/', views.PledgeDetail.as_view()),
  path('sports/', views.SportList.as_view()),
  path('sports/<int:pk>/', views.SportDetail.as_view()),
  path('clubs/', views.Clublist.as_view()),
  path('clubs/<int:pk>/', views.ClubDetail.as_view()),
]