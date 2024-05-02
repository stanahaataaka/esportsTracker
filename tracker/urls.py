from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('teams/', views.TeamListView.as_view(), name='teams'),
    path('teams/<str:pk>', views.TeamDetailView.as_view(), name='teams'),
    path('players/', views.PlayerListView.as_view(), name='players'),
    path('matches/', views.MatchListView.as_view(), name="matches"),
    path('matches/<str:pk>', views.MatchDetailView.as_view(), name = "matches")
]
