from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('teams/', views.TeamListView.as_view(), name='teams'),
    path('teams/<str:pk>', views.TeamDetailView.as_view(), name='teams'),
<<<<<<< HEAD
    path("admin_tracker/", views.admin_tracker, name="admin_tracker")
=======
    path('players/', views.PlayerListView.as_view(), name='players'),
>>>>>>> main
]
