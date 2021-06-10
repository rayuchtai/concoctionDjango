from django.urls import path
from . import views

urlpatterns = [
    path('api/worlds', views.WorldList.as_view(), name='world_list'),
    path('api/worlds/<int:pk>', views.WorldDetail.as_view(), name='world_detail'),
]
