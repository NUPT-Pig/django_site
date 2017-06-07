from django.conf.urls import include, url

urlpatterns = [
    url(r'^login/$', StudentsView.as_view(), name='list_create_students'),
]