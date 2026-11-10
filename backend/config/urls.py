from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # API Urls
    path('api/categories/', include('categories.urls')),
    path('api/feedback/', include('feedback.urls')),

    #frontend pages
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('feedback/', feedback, name='feedback'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )