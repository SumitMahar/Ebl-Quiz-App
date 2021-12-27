from django.urls import path
from .views import register, logout_view


app_name = 'accounts'
urlpatterns = [
    # path('logout/', logout_view, name='logout'),
    path('signup/', register, name='signup')
]