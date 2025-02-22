"""djangoproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
import os  # Import os for path operations

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),
    path('', TemplateView.as_view(template_name="Home.html")),
    path('about/', TemplateView.as_view(template_name="About.html")),
    path('contact/', TemplateView.as_view(template_name="Contact.html")),
    path('login/', TemplateView.as_view(template_name="index.html")),
    path('register/', TemplateView.as_view(template_name="index.html")),
    path('dealers/', TemplateView.as_view(template_name="index.html")),
    path(
        'dealer/<int:dealer_id>/',
        TemplateView.as_view(template_name="index.html")
        ),
    path(
        'postreview/<int:dealer_id>/',
        TemplateView.as_view(template_name="index.html")
        ),
    # Serve the manifest.json file
    re_path(
        r'^manifest.json$',
        serve,
        {'document_root': os.path.join(
            settings.BASE_DIR, 'frontend/build'),
            'path': 'manifest.json'}
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Add a newline at the end of the file