from django.core.management.base import BaseCommand, CommandError
from app import app_name

class Command(BaseCommand):

    def add_arguments(self, parser):

         parser.add_argument(
            '-args',
            '--args',
            action='store',
            dest='args',
            default='close',
            help='args',
        )

    def handle(self, *args, **options):
        try:
            if options['args']:
                print('hello world, %s' % options['name'])
            
            self.stdout.write(self.style.SUCCESS('命令%s执行成功, 参数为%s' % (__file__, options['name'])))
        except Exception as ex:
            self.stdout.write(self.style.ERROR('命令执行出错'))