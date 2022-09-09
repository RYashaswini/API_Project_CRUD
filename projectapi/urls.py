from django.urls import path
from projectapi import views


urlpatterns=[
    path('index/',views.index,name="index"),
    path('create/',views.create,name="create"),
    path('retrieve/',views.retrieve,name="retrieve"),
    path('updateobj/<int:id>/',views.updateobj,name="updateobj"),
    path('deleteobj/<int:id>/',views.deleteobj,name='deleteobj'),

]