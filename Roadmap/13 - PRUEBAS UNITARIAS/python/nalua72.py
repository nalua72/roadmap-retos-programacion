import unittest
from datetime import datetime, date

# Function to add two numbers, raises ValueError if inputs are not numbers
def add_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both arguments must be numbers.")
    return a + b

# Unit tests for add_numbers function
class TestAddNumbers(unittest.TestCase):
    def test_add_integers(self):
        # Test addition of two integers
        self.assertEqual(add_numbers(1, 2), 3)

    def test_add_floats(self):
        # Test addition of two floats
        self.assertAlmostEqual(add_numbers(1.5, 2.5), 4.0)

    def test_add_mixed(self):
        # Test addition of integer and float
        self.assertAlmostEqual(add_numbers(1, 2.5), 3.5)

    def test_add_negative(self):
        # Test addition of negative numbers
        self.assertEqual(add_numbers(-1, -1), -2)

    def test_add_zero(self):
        # Test addition with zero
        self.assertEqual(add_numbers(0, 5), 5)
        self.assertEqual(add_numbers(5, 0), 5)

    def test_invalid_input(self):
        # Test invalid inputs (non-numeric)
        with self.assertRaises(ValueError):
            add_numbers("a", 2)
        with self.assertRaises(ValueError):
            add_numbers(1, "b")
        with self.assertRaises(ValueError):
            add_numbers(None, 2)
        with self.assertRaises(ValueError):
            add_numbers(1, None)

""" EXTRA """

# Example user data dictionary
User = {
    "name": "Jose Rodriguez",
    "age": 53,
    "birtday": datetime.strptime("10-07-72", "%d-%m-%y").date(),
    "programming_languages": ["Python", "JavaScript", "Lua", "C++"],
    }

# Unit tests for User data dictionary
class TestUserData(unittest.TestCase):
    def test_user_fields(self):
        # Test that all required fields exist
        self.assertIn("name", User)
        self.assertIn("age", User)
        self.assertIn("birtday", User)
        self.assertIn("programming_languages", User)

    def test_user_types(self):
        # Test that fields have correct types
        self.assertIsInstance(User["name"], str)
        self.assertIsInstance(User["age"], int)
        self.assertIsInstance(User["birtday"], date)
        self.assertIsInstance(User["programming_languages"], list)

# Run unit tests if this file is executed directly
if __name__ == "__main__":
    unittest.main()
