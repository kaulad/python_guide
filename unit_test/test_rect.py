""" Unit test for my rect
pytest unit test -v
pytest -v
pytest -m basic
pytest --help
"""
# import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from example_good_pep8 import MyRect

# to run pytest -m basic
@pytest.mark.basic
def test_say_hello():
    """Test printing"""
    print('say hello')

@pytest.mark.skip
def test_skip():
    """Test skpping"""
    print('skipping')

# @pytest.mark.function
# def test_can_compute_area():
#     """ Test compte area"""
#     rect = MyRect(4,5)
#     assert rect.compute_area() == 21, "formula is incorrect"
