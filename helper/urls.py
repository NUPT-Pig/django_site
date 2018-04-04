from django.conf.urls import include, url
from helper.views import AccountView, AccountDetailView, TestView

urlpatterns = [
    url(r'^account/$', AccountView.as_view(), name='account'),
    url(r'^account_detail/(?P<pk>\d+)/$', AccountDetailView.as_view(), name='account_detail'),
    url(r'test/$', TestView.as_view())
]