import unittest
import csv

from model.user.User import User


class TestUser(unittest.TestCase):
    _users = []
    _file_location = "./tests/mock-data/users.csv"

    def setUp(self):
        with open(self._file_location, mode="r", newline="") as csv_file:
            csv_reader = csv.DictReader(
                csv_file,
                fieldnames=User.field_names(),
            )
            for index, row in enumerate(csv_reader):
                if index == 0:
                    continue
                self._users.append(User(row["id"], row["user_name"]))

    def test_static_user_field_names(self):
        self.assertEqual(User.field_names(), ["id", "user_name"])

    def test__dict__returns_user_values_as_dict(self):
        self.assertEqual(
            self._users[0].__dict__(),
            {"id": "test-id-1", "user_name": "test_subject-1"},
        )
