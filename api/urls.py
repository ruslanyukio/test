from django.contrib import admin
from django.urls import path, include
from . import views as vs

urlpatterns = [
	path('', vs.Page.as_view())
]