import os

from common_interface.log_interface import get_logger
logger = get_logger('students_supporter')

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def handle(self, *args, **options):
        os.system("echo %d > %s" % (os.getpid(), '/home/anshun/TEST/log/hr.txt'))
        logger.info('students')