from common_interface.log_interface import get_logger
logger = get_logger('all_supporters')

import daemon
import os
import subprocess
import time
import signal

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from common_interface.const import PathConst


class Command(BaseCommand):

    def __init__(self):
        super(Command, self).__init__()
        self.children = []
        self.is_stop = False

    def add_arguments(self, parser):
        parser.add_argument('action', type=str)

    def handle_quit(self, signum, frame): # these two parameters must be included. Or this method may not be executed.
        logger.info('handle quit signal')
        self.is_stop = True
        os.system("echo %s > %s" % ('quit signal received', PathConst.DAEMON_LOG))

    def start(self):
        with daemon.DaemonContext():
            logger = get_logger('all_supporters')   #logger takes no effect
            #print logger.name
            logger.info('Daemon pid is %s' % os.getpid())
            os.system("echo %d > %s" % (os.getpid(), PathConst.SUPPORTERS_DAEMON_PID))

            signal.signal(signal.SIGTERM, self.handle_quit)

            #os.system("python /home/anshun/python/django_site/manage.py students_supporter")
            child = subprocess.Popen(['python', os.path.join(settings.BASE_DIR, 'manage.py'), 'students_supporter'])
            self.children.append(child)

            while not self.is_stop:
                time.sleep(60*60)

            for child in self.children:
                #A None value indicates that the process hasn't terminated yet.
                # A negative value -N indicates that the child was terminated by signal N (Unix only).
                if child.poll() is None:
                    child.terminate()
            for child in self.children:
                child.wait()

            os.remove(PathConst.SUPPORTERS_DAEMON_PID)

    def stop(self):
        if os.path.exists(PathConst.SUPPORTERS_DAEMON_PID):
            with open(PathConst.SUPPORTERS_DAEMON_PID, 'r') as f:
                pid = int(f.read())
                logger.info('stop pid %d' % pid)
                os.kill(pid, signal.SIGTERM)

    def handle(self, *args, **options):
        if options['action'] == 'start':
            logger.info('start all supporters')
            self.start()
        elif options['action'] == 'stop':
            logger.info('stop all supporters')
            self.stop()
