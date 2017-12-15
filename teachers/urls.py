from django.conf.urls import include, url

from teachers.views import TeachersView

urlpatterns = [
    url(r'^$', TeachersView.as_view(), name='list_create_teachers'),
]