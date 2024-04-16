from behave import *
from test import *


@given('a Zombie site')
def step_impl(context):
    context.zombie = Zombie()

@then('open home page')
def step_impl(context):
    context.zombie.open_site()

@then('test element home')
def test_element(context):
    context.zombie.test_element_home()

@then('test element blog')
def test_element(context):
    context.zombie.test_element_blog()

@then('test element brains')
def test_element(context):
    context.zombie.test_element_brains()

@then('test element more')
def test_element_more(context):
    context.zombie.test_element_more()

@then('test element regular')
def test_element_regular(context):
    context.zombie.test_element_regular()

@then('test element lite')
def test_element_lite(context):
    context.zombie.test_element_lite()

@then('close window')
def test_element_lite(context):
    context.zombie.test_close_driver()

@then('I should see exect options {expected_count:d}')
def options_count(context, expected_count):
    context.zombie.options_count(expected_count)
    



