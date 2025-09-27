
import sys
import os

# Add the src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.main import hello_world

def test_hello_world():
    assert hello_world() == "Hello, World!"