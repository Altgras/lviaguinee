from django.urls import path
from . import views

urlpatterns = [
    path('',views.readers,name="readers"),
    path('addreader/',views.add_reader,name="add-reader"),
]