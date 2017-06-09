from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('action', type=str)

    def start(self):
        pass

    def handle(self, *args, **options):
        print options
        if options['action'] == 'start':
            self.start()