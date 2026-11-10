from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.http import JsonResponse


def cors_diagnostic(request):
    return JsonResponse({
        "settings_module": settings.SETTINGS_MODULE,
        "cors_allowed_origins": getattr(
            settings, "CORS_ALLOWED_ORIGINS", []
        ),
        "cors_middleware_enabled": any(
            "corsheaders.middleware.CorsMiddleware" == middleware
            for middleware in settings.MIDDLEWARE
        ),
    })



urlpatterns = [
    path('admin/', admin.site.urls),

    # API Urls
    path('api/cors-check/', cors_diagnostic),
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