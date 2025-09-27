
import pytest
from src.main import hello_world

def test_hello_world_return():
    assert hello_world() == "Hello, World!"

def test_hello_world_type():
    assert isinstance(hello_world(), str)