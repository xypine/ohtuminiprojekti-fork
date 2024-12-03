import unittest
from validate import validate_inproceedings, UserInputError
from config import app


class TestValidator(unittest.TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        self.valid_data = {
            "reference_id": "ref001",
            "author": "John Doe",
            "title": "An Innovative Approach to AI",
            "booktitle": "Proceedings of the AI Conference",
            "year": "2024",
            "editor": "Jane Smith",
            "volume": "1",
            "number": "1",
            "series": "AI Series",
            "pages": "1-10",
            "address": "New York, NY",
            "month": "November",
            "organization": "AI Society",
            "publisher": "Tech Press",
        }

    def test_input_not_string(self):
        data = self.valid_data.copy()
        data["reference_id"] = 123
        with self.assertRaises(UserInputError):
            validate_inproceedings(**data)

    def test_input_negative_int(self):
        data = self.valid_data.copy()
        data["volume"] = "-5"
        with self.assertRaises(UserInputError):
            validate_inproceedings(**data)

    def test_input_negative_year(self):
        data = self.valid_data.copy()
        data["year"] = "3020"
        with self.assertRaises(UserInputError):
            validate_inproceedings(**data)

    def test_invalid_month(self):
        data = self.valid_data.copy()
        data["month"] = "Octember"
        with self.assertRaises(UserInputError):
            validate_inproceedings(**data)

    def test_required_field_missing(self):
        data = self.valid_data.copy()
        del data["title"]
        with self.assertRaises(TypeError):
            validate_inproceedings(**data)

    def test_valid_input(self):
        try:
            validate_inproceedings(**self.valid_data)
        except UserInputError:
            self.fail(
                "validate_inproceedings raised UserInputError unexpectedly!")

    def tearDown(self):
        self.app_context.pop()