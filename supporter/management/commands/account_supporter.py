import os


from openpyxl import Workbook

from helper.models import Account

from common_interface.log_interface import get_logger
logger = get_logger('account_supporter')

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('action', type=str)
        parser.add_argument('--time', default=None, help='select the year or month you want to export ex. 201801 ')

    def export(self, **options):
        wb = Workbook()
        sheet = wb.create_sheet('account', index=0)
        sheet.append(['编号', '用户', '金额', '备注', '文件地址'])
        if len(options['time']) == len('201801'):
            month = options['time'][-2:]
            #logger.info(month)
            year = options['time'][0:4]
            #logger.info(year)
            for account in Account.objects.all().filter(date__year=int(year), date__month=int(month)):
                #logger.info(account.id)
                sheet.append([account.id, account.user.username, account.money, account.comment, account.file.name])
        elif len(options['time']) == len('2018'):
            year = options['time'][0:4]
            for account in Account.objects.all().filter(date__year=int(year)):
                sheet.append([account.id, account.user.username, account.money, account.comment, account.file.name])
        else:
            logger.error('wrong time format in export accounts')
            return False
        wb.save(settings.MEDIA_ROOT + 'account/' + options['time'] + '.xlsx')


    def handle(self, *args, **options):
        logger.info('start account supporter')
        try:
            if options['action'] == 'export':
                logger.info('%s' % options)
                self.export(**options)
            else:
                logger.error("wrong options")
        except Exception as e:
            logger.error('%s' % str(e))