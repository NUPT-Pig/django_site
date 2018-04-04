from django.conf.urls import include, url
from helper.views import AccountView, TestView

urlpatterns = [
    url(r'^add_account/$', AccountView.as_view(), name='add_account'),
    url(r'test/$', TestView.as_view())
]