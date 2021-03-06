"""django_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, static
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^students/', include('students.urls')),
    url(r'^teachers/', include('teachers.urls')),
    url(r'^tasks/', include('tasks.urls')),
    url(r'^management/', include('management.urls')),
    url(r'upload_files/', include('upload_files.urls')),
    url(r'helpers/', include('helper.urls'))
]


urlpatterns += [
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^$', static.serve, {'path': 'index.html', 'document_root': settings.STATIC_ROOT}),
    url(r'(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}),
]