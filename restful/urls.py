from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', include('drones.urls')),

    # not work as in the book;;; irrelevant to the site
    # path('api-auth/', include('rest_framework.urls')),
    path('login/', obtain_auth_token, name='obtain_auth_token'),

]

