from django.conf.urls import include, url
from students.views import StudentsView

urlpatterns = [
    url(r'^$', StudentsView.as_view(), name='list_create_students'),
]