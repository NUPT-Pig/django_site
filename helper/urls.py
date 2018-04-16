from django.conf.urls import include, url
from helper.views import AccountView, AccountDetailView, AccountCheckView, TestView

urlpatterns = [
    url(r'^account/$', AccountView.as_view(), name='account'),
    url(r'^account_detail/(?P<pk>\d+)/$', AccountDetailView.as_view(), name='account_detail'),
    url(r'account_check/(?P<pk>\d+)/$', AccountCheckView.as_view(), name='account_check'),
    url(r'test/$', TestView.as_view())
]