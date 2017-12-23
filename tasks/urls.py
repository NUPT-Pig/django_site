from django.conf.urls import url

from tasks.views import TasksView, TaskDetailView

urlpatterns = [
    url(r'^$', TasksView.as_view(), name="create_list_tasks"),
    url(r'detail/(?P<pk>\d+)/$', TaskDetailView.as_view(), name="detail_task"),
]