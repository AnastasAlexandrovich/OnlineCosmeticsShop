import os
import django
from behave import fixture, use_fixture
from django.test.runner import DiscoverRunner
from django.test.testcases import LiveServerTestCase, TestCase

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Onlineshop.settings')
django.setup()


def before_all(context):
    context.test_runner = DiscoverRunner()
