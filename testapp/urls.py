from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('ayax/', include('ayax.urls')),
    path('admin/', admin.site.urls),
]
