from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('branch.urls')),
    path('', include('news.urls')),
    path('auth/', include('rest_framework.urls'))
]