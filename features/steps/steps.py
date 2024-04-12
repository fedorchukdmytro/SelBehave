from behave import *
from test import *


@given('a Zombie site')
def step_impl(context):
    context.zombie = Zombie()

@when('open home page')
def step_impl(context):
    context.zombie.open_site()

@when('check link home')
def check_link(context):
    context.zombie.check_link_home()

@when('check link blog')
def check_link(context):
    context.zombie.check_link_blog()

@when('check link brains')
def check_link(context):
    context.zombie.check_link_brains()


@when('set text in field')
def step_impl(context):
    context.zombie.search()

# @then('see the list result of search')
# def step_impl(context):
#     context.google.see_list()