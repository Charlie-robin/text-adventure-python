import csv
import unittest

from model.user.UserRepository import UserRepository
from model.user.User import User

class TestUserRepository(unittest.TestCase):
    _file_location = "./tests/mock-data/users.csv"
    _user_repository = UserRepository(_file_location)
    _test_data = [
        {"id": "test-id-1", "user_name": "test_subject-1"},
        {"id": "test-id-2", "user_name": "test_subject-2"},
    ]

    def setUp(self):
        self._user_repository.current_user = None
        with open(self._file_location, mode="w", newline="") as csv_file:
            csv_writer = csv.DictWriter(
                csv_file,
                fieldnames=User.field_names(),
            )
            csv_writer.writeheader()
            for data in self._test_data:
                csv_writer.writerow(data)

    def test_get_user_by_id_finds_user_with_matching_id(self):
        result = self._user_repository.get_user_by_id("test-id-1")
        self.assertEqual(result.id, "test-id-1")
        self.assertEqual(result.user_name, "test_subject-1")

    def test_get_user_by_id_returns_user(self):
        result = self._user_repository.get_user_by_id("test-id-2")
        self.assertTrue(type(result) is User)

    def test_get_user_by_id_finds_user_with_matching_id(self):
        with self.assertRaises(Exception):
            self._user_repository.get_user_by_id("no-match")

    def test_get_all_users_gets_matches_data_from_csv(self):
        results = self._user_repository.get_all_users()
        for result in results:
            self.assertTrue(type(result) is User)

    def test_get_all_users_returns_user(self):
        results = self._user_repository.get_all_users()
        for index, result in enumerate(results):
            self.assertEqual(result.id, self._test_data[index]["id"])

    def test_create_user_adds_user_to_csv(self):
        self._user_repository.create_user("charlie")
        result = self._get_rows_from_csv()[-1]
        self.assertEqual(result["user_name"], "charlie")

    def _get_rows_from_csv(self):
        with open(self._file_location, mode="r", newline="") as csv_file:
            csv_reader = csv.DictReader(
                csv_file,
                fieldnames=User.field_names(),
            )
            rows = []
            for row in csv_reader:
                rows.append(row)
            return rows
