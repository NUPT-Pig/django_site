from django.conf import settings
import os


class PathConst(object):
    SUPPORTERS_DAEMON_PID = os.path.join(settings.BASE_DIR, 'django_site/log/supporters.pid')
    LOG_FOLDER = os.path.join(settings.BASE_DIR, 'django_site/log/')
    #LOG_FOLDER = '/var/log/django/'
    DAEMON_LOG = os.path.join(settings.BASE_DIR, 'django_site/log/daemon.log')

