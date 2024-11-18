from django.contrib import admin
from django.urls import include, path

from recipes.views import RedirectViewSet

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/', include('api.urls'), name='api'),
    path('redirect/<str:short_code>/',
         RedirectViewSet.as_view({'get': 'redirect_short_link'}),
         name='short_link_redirect'),
]
