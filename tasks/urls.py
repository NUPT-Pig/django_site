from django.conf.urls import url

from tasks.views import TasksView, TaskDetailView, TaskCreateView, TaskDestroyView

urlpatterns = [
    url(r'^$', TasksView.as_view(), name="list_tasks"),
    url(r'create/$', TaskCreateView.as_view(), name="create_task"),
    url(r'delete/$', TaskDestroyView.as_view(), name='delete_tasks'),
    url(r'detail/(?P<pk>\d+)/$', TaskDetailView.as_view(), name="detail_task"),
]