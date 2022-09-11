import csv
import uuid

from model.User import User


class UserRepository:
    _file_location = "./data/users.csv"
    _current_user = None

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

    @property
    def current_user(self):
        return self._current_user
