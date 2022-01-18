import os
import django
from django.test.runner import DiscoverRunner

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Onlineshop.settings')
django.setup()


def before_all(context):
    context.test_runner = DiscoverRunner()
