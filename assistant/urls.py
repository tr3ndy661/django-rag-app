from django.urls import include, path
from . import views

urlpatterns = [
    path("ask/", views.ask, name='main-view')
]