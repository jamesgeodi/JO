# test_jooqgenerator.py
"""
Tests for JOOQGenerator module.
"""

import unittest
from jooqgenerator import JOOQGenerator

class TestJOOQGenerator(unittest.TestCase):
    """Test cases for JOOQGenerator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = JOOQGenerator()
        self.assertIsInstance(instance, JOOQGenerator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = JOOQGenerator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
