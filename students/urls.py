from django.conf.urls import include, url
from students.views import StudentsView, StudentDetailView

urlpatterns = [
    url(r'^$', StudentsView.as_view(), name='list_create_students'),
    url(r'detail/(?P<pk>\d+)/$', StudentDetailView.as_view(), name='detail_update_destory_student')
]