from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # API Urls
    path('api/categories/', include('categories.urls')),

    #frontend pages
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('feedback/', feedback, name='feedback'),
]
