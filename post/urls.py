from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name="index"),
    path('list/',views.list_view,name="list"),
    path('detail/<id>',views.detail_view,name="Detail"),
    path('update/<id>',views.update_view,name="Update"),
    path('create/',views.create_view,name="Create"),
    path('delete/<id>',views.delete_view,name="Delete"),
]