"""
This module contains basic math unit tests.
These are examples using the pytest framework.
This is from the course at test automation univeristy, pytest
"""

import pytest

# ---------------------------------
# A simple test
# ---------------------------------
def test_one_plus_one():
  assert 1 + 1 == 2

# ---------------------------------
# Assertion introspection
# ---------------------------------
def test_one_plus_two():
  a = 1
  b = 2
  c = 3
  assert a + b == c


# ---------------------------------
# Verifying an exception
# ---------------------------------
def test_divide_by_zero():
  with pytest.raises(ZeroDivisionError) as err:
    num = 1 / 0

  assert 'division by zero' in str(err.value)


# ---------------------------------
# A parametrized function
# ---------------------------------

products_tuple = [
  (2, 3, 6),                  # postive integers
  (1, 99, 99),                # identity
  (0, 99, 0),                 # zero
  (3, -4, -12),               # positive by negative
  (-5, -5, 25),     	        # negative by negative
  (2.5, 6.7, 16.75)           # floats
]


@pytest.mark.parametrize('a, b, product', products_tuple)
def test_multiplication(a, b, product):
  assert a * b == product



