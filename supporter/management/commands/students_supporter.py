import os

from common_interface.log_interface import get_logger
logger = get_logger('students_supporter')

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.info('start students supporter')
        try:
            while True:
                pass
        except Exception as e:
            logger.error('%s' % str(e))
