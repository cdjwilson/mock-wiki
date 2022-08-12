from django.urls import path

from . import views

urlpatterns = [
    path("wiki", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("wiki/<str:title>/edit", views.edit, name="edit"),
    path("wiki/create/new", views.new, name="new"),
    path("random", views.randomEntry, name="randomEntry"),
    path("wiki/<str:title>/delete", views.deleteEntry, name="deleteEntry")
]
