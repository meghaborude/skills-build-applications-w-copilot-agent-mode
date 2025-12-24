import os
from django.http import JsonResponse
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
]
def api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME', None)
    if codespace_name:
        api_url = f"https://{codespace_name}-8000.app.github.dev"
        # Optionally, you can add a warning about HTTPS certificate issues
        return JsonResponse({
            "api_url": api_url,
            "note": "If you encounter HTTPS certificate issues, try using an incognito window or accept the certificate warning."
        })
    else:
        return JsonResponse({
            "error": "CODESPACE_NAME environment variable not set."
        }, status=500)

urlpatterns += [
    path('api/', api_root),
]
"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
