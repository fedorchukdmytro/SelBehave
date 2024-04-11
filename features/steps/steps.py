from behave import *
from test import *
# from selene import *

@given('a Google')
def step_impl(context):
    context.google = Google()

@when('open Google page')
def step_impl(context):
    context.google.open_site()

@when('check link {images}')
def check_link(context, images):
    context.google.check_link(images)


@when('set text in field')
def step_impl(context):
    context.google.search()

# @then('see the list result of search')
# def step_impl(context):
#     context.google.see_list()