from django.conf.urls import include, url

from teachers.views import TeachersView, TeachersDetailView, MyDetailView, TeachersCheckView

urlpatterns = [
    url(r'detail/(?P<pk>\d+)/$', TeachersDetailView.as_view(), name='teacher_detail'),
    url(r'MyDetail/', MyDetailView.as_view(), name='my_detail'),
    url(r'check/', TeachersCheckView.as_view(), name='check'),
    url(r'^$', TeachersView.as_view(), name='list_create_teachers'),
]