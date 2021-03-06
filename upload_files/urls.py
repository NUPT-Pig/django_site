from django.conf.urls import include, url

from upload_files.views import UploadTextView, TextListView, UploadMediaView

urlpatterns = [
    url(r'^text/upload/$', UploadTextView.as_view(), name='upload_text'),
    url(r'^text/$', TextListView.as_view(), name='list_text'),
    url(r'^media/upload/$', UploadMediaView.as_view(), name='upload_media'),
]