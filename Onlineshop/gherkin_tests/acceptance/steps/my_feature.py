import json
from datetime import datetime, timezone

import pytz
import requests
from behave import *
from django.http import JsonResponse

from catalog.models import Manufacturer, Type, Product
import nose.tools
from django.test import Client

from core.models import User
from order.models import ProductAmount, Order

from rest_framework.test import force_authenticate, APIRequestFactory

from order.views import OrderListView
from order.serializers import OrderSerializer

use_step_matcher("re")


@given('create products')
def step_impl(context):

    a = Manufacturer.objects.create(name="Loreal")
    t = Type.objects.create(name="Помада")
    Product.objects.create(name="супер помада 1", description="1", price=10, seller=a, in_stock=1, type=t)
    Product.objects.create(name="супер помада 2", description="2", price=10, seller=a, in_stock=3, type=t)
    Product.objects.create(name="супер помада 3", description="3", price=10, seller=a, in_stock=5, type=t)


@when('user gets product')
def step_impl(context):
    c = Client()
    context.res = c.get("/products/" + context.table[0]['id'])
    nose.tools.assert_equal(context.res.status_code, 200)

@then('validate results')
def step_impl(context):
    res = context.res.json()
    nose.tools.assert_true(res['name'], "супер помада 1")


# ---------------------------------------------- another scenario ---------------------------------------------- #


@given("prepare data")
def step_impl(context):

    User.objects.create(email="user@mail.ru", username="user", password="password",
                            first_name="User", last_name="User", second_name="User", created_at=datetime.now())
    u = User.objects.get(pk=1)
    u.is_active=True
    u.save()
    context.u = u

    a = Manufacturer.objects.create(name="Loreal")
    t = Type.objects.create(name="Помада")
    p = Product.objects.create(name="супер помада 1", description="1", price=10, seller=a, in_stock=1, type=t)
    product_amount = ProductAmount.objects.create(product=p, amount=2)
    o = Order.objects.create(orderer=u, date_of_order=datetime.now(),
                             address="Some address", date_of_delivery=datetime.now(),
                             status="Новый")
    o.product_amount.add(product_amount)


@when("user gets orders")
def step_impl(context):

    view = OrderListView.as_view()
    factory = APIRequestFactory()
    request = factory.get('/orderlist/')
    force_authenticate(request, user=context.u)
    response = view(request)

    context.response_order = response


@then("validate orders")
def step_impl(context):
    nose.tools.assert_equal(context.response_order.status_code, 200)
    nose.tools.assert_true(context.response_order.data)