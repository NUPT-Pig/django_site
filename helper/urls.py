from django.conf.urls import include, url
from helper.views import AccountView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
]