from django.urls import path

from recipes.views import short_link_redirect

urlpatterns = [
    path('s/<str:short_code>/', short_link_redirect,
         name='short_link_redirect'),
]
