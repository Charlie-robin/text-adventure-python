import csv
import uuid

from model.user.User import User


class UserRepository:
    def __init__(self, file_location):
        self._file_location = file_location
        self._current_user = None

    def create_user(self, user_name):
        user = User(uuid.uuid4(), user_name)
        self._append_user_to_csv(user)
        self._current_user = user

    def _append_user_to_csv(self, user):
        with open(self._file_location, mode="a", newline="") as csv_file:
            csv_writer = csv.DictWriter(
                csv_file,
                fieldnames=User.field_names(),
            )
            csv_writer.writerow(user.__dict__())

    def get_user_by_id(self, id):
        with open(self._file_location, mode="r", newline="") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                if id == row["id"]:
                    self._current_user = User(row["id"], row["user_name"])

            if not self._current_user:
                raise Exception("No User Found")

            return self._current_user

    def get_all_users(self):
        with open(self._file_location, mode="r", newline="") as csv_file:
            csv_reader = csv.DictReader(
                csv_file,
                fieldnames=User.field_names(),
            )
            users = []
            for index, row in enumerate(csv_reader):
                if index == 0:
                    continue
                users.append(User(row["id"], row["user_name"]))
            return users

    @property
    def current_user(self):
        return self._current_user

    @current_user.setter
    def current_user(self, value):
        self._current_user = value
