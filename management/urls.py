from django.conf.urls import include, url
from management.views import LoginView, RegisterView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
]