from django.urls import path
from confessapp import views

urlpatterns = [
    path("", views.index, name="seeallposts"),
    path("registerconfession/", views.registerconfession, name="registerconfession")
]