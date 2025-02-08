from pathlib import Path
import pytest
import pathlib
from pathlib import Path
import pytest
from mypy.types import names
from unicodedata import category

from tests.conftest import product

# from tests.conftest import product

current_dir = Path(__file__).parent.parent.resolve()
cover_main = current_dir/'src'/'category.py'


from src.category import Category
from src.product import Product


def test_add_product(first_category1):
    assert first_category1.product_count == 3