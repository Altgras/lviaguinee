from django.urls import path
from . import views

urlpatterns = [
    path('',views.borrows,name="borrows"),
    path('addborrow/',views.add_borrow,name="add-borrow"),
    path('returns/',views.returns,name="returns")
]