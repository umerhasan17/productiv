from django.contrib import admin
from django.urls import include, path
from .routers import router

urlpatterns = [
    path('app/', include('app.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]