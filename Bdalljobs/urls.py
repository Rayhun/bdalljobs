"""Bdalljobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# DJANGO IMPORTS
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from django.urls import include, path
# CORE IMPORTS
from Core.views import IndexView, SignupView, LoginView, Sign_upView


from .sitemaps import (
    StaticViewSitemap, JobsPostSiteMap
)

sitemaps = {
    'static': StaticViewSitemap,
    'job_post': JobsPostSiteMap,
}

urlpatterns = [
    # index url ---------------------------------------------------------------
    path('', IndexView.as_view(), name='index'),

    # prometheus url ----------------------------------------------------------
    path('', include('django_prometheus.urls')),

    # admin urls --------------------------------------------------------------
    path(f'{settings.ADMIN_URL}/', admin.site.urls),

    # Core urls ---------------------------------------------------------------
    path('core/', include('Core.urls')),

    # jobs urls ---------------------------------------------------------------
    path('jobs/', include('jobs.urls')),

    # company urls ------------------------------------------------------------
    path('company/', include('company.urls')),

    # API urls ----------------------------------------------------------------
    path('api/', include('API.urls')),

    # auth urls ---------------------------------------------------------------
    path('auth/signup/', SignupView.as_view(), name='signup'),
    path('auth/sign_up/', Sign_upView.as_view(), name='sign_up'),
    path('auth/signin/', LoginView.as_view(), name='signin'),
    path('auth/', include('django.contrib.auth.urls')),
    path('core/', include('Core.urls')),
    # drf api auth ------------------------------------------------------------
    path('api-auth/', include('rest_framework.urls')),

    # ckeditor ----------------------------------------------------------------
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    # robots.txt
    path(
        'robots.txt',
        TemplateView.as_view(
            template_name="Core/robots.txt", content_type="text/plain"
        )
    )
]

# serve media files in development environment --------------------------------
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

# debug toolbar ---------------------------------------------------------------
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

# admin site customizations ---------------------------------------------------
admin.sites.AdminSite.site_header = "All Jobs In Bd Administration"
admin.sites.AdminSite.site_title = "All Jobs In Bd Administration"
admin.sites.AdminSite.index_title = "All Jobs In Bd Admin Panel"
