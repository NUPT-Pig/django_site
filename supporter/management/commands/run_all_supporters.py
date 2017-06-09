from common_interface.log_interface import get_logger
logger = get_logger('all_supporters')

import daemon
import os
import subprocess

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('action', type=str)

    def start(self):
        with daemon.DaemonContext():
            logger = get_logger('all_supporters')   #logger takes no effect
            #print logger.name
            logger.info('Daemon pid is %s' % os.getpid())
            os.system("echo %d > %s" % (os.getpid(), '/home/anshun/TEST/log/student.txt'))
            os.system("python /home/anshun/python/django_site/manage.py students_supporter")
            subprocess.Popen(['python', '/home/anshun/python/django_site/manage.py', 'students_supporter'])

    def handle(self, *args, **options):
        if options['action'] == 'start':
            logger.info('start all supporters')
            self.start()