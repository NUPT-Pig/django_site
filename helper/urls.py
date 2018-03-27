from django.conf.urls import include, url
from helper.views import AccountView

urlpatterns = [
    url(r'^add_account/$', AccountView.as_view(), name='add_account'),
]