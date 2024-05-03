from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("admin_tracker/", views.admin_tracker, name="admin_tracker"),
    path('teams/', views.TeamListView.as_view(), name='teams'),
    path('teams/<str:pk>', views.TeamDetailView.as_view(), name='team-detail'),
    path('players/', views.PlayerListView.as_view(), name='players'),
    path('players/<str:pk>', views.PlayerDetailView.as_view(), name='player-detail'),
]

urlpatterns += [
    path('teams/create/', views.TeamCreate.as_view(), name='team-create'),
    path('teams/<str:pk>/update/', views.TeamUpdate.as_view(), name='team-update'),
    path('teams/<str:pk>/delete/', views.TeamDelete.as_view(), name='team-delete'),
]

urlpatterns += [
    path('players/create/', views.PlayerCreate.as_view(), name='player-create'),
    path('players/<str:pk>/update/', views.PlayerUpdate.as_view(), name='player-update'),
    path('players/<str:pk>/delete/', views.PlayerDelete.as_view(), name='player-delete'),
]

urlpatterns += [
    path('matches/create/', views.PlayerCreate.as_view(), name='match-create'),
    path('matches/<str:pk>/update/', views.PlayerUpdate.as_view(), name='match-update'),
    path('matches/<str:pk>/delete/', views.TeamDelete.as_view(), name='match-delete'),
]