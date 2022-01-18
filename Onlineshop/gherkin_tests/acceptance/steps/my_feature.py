from behave import *

from catalog.models import Manufacturer
from nose.tools import assert_equal

use_step_matcher("re")


@given('we have behave installed')
def step_impl(context):
    context.model = Manufacturer
    for raw in context.table:
        context.model.objects.create(name=raw['name'])

    qs = Manufacturer.objects.all()
    assert_equal(len(qs), 2)


@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False