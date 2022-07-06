from django.urls import path
from apps.login.api.api import user_api_view,user_detail_view

urlpatterns = [
    path('usuario/', user_api_view, name='usuario_fun'),
    path('usuario/<int:pk>', user_detail_view, name ='usuario_datail'),
]
