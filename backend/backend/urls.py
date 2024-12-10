from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/', include('api.urls'), name='api'),
    path('recipes/', include('recipes.urls'), name='recipes'),
]
