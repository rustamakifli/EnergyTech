from django.urls import path

from custom_admin import views


urlpatterns = [
    path("scoreboard/", views.Scoreboard.as_view(), name="scoreboard")
]