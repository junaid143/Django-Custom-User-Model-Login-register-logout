from django.urls import path
from . import views


urlpatterns = [
    path('' , views.Home_view , name = 'home'),
    path('register/' , views.register_view.as_view() , name = 'register'),
    path('signout/' , views.signout , name = 'signout'),
]