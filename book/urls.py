from django.urls import path
from . import views

urlpatterns = [
    path('',views.books,name="books"),
    path('readpoints/',views.read_points,name="readpoints"),
    path('ranks/',views.ranks,name="ranks"),
    path('edit/<int:id>/',views.ranks,name="edit-book")
]