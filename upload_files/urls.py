from django.conf.urls import include, url

from upload_files.views import UploadTextView

urlpatterns = [
    url(r'^text/$', UploadTextView.as_view(), name='upload_text'),
]