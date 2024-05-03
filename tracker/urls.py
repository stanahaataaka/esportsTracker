from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("admin_tracker/", views.GameListView.as_view(), name="admin_tracker"),
    path("matches/", views.MatchListView.as_view(), name="matches"),
    path('teams/', views.TeamListView.as_view(), name='teams'),
    path('teams/<int:pk>', views.TeamDetailView.as_view(), name='team-detail'),
    path('players/', views.PlayerListView.as_view(), name='players'),
    path('players/<int:pk>', views.PlayerDetailView.as_view(), name='player-detail'),
    path('games/<int:pk>', views.GameDetailView.as_view(), name='game-detail'),
]

urlpatterns += [
    path('teams/create/', views.TeamCreate.as_view(), name='team-create'),
    path('teams/<int:pk>/update/', views.TeamUpdate.as_view(), name='team-update'),
    path('teams/<int:pk>/delete/', views.TeamDelete.as_view(), name='team-delete'),
]

urlpatterns += [
    path('players/create/', views.PlayerCreate.as_view(), name='player-create'),
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='player-update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='player-delete'),
]

urlpatterns += [
    path('games/create/', views.GameCreate.as_view(), name='game-create'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='game-update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='game-delete'),
]

#urlpatterns += [
#    path('matches/create/', views.MatchCreate.as_view(), name='match-create'),
#    path('matches/<str:pk>/update/', views.MatchUpdate.as_view(), name='match-update'),
#    path('matches/<str:pk>/delete/', views.MatchDelete.as_view(), name='match-delete'),
#]