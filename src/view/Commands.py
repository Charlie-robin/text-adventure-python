from view.TextFormatter import TextFormatter


class Commands:
    _line_width = 50

    def __init__(self, commands, start=1):
        self._commands = commands
        self._start = start
        self._limit = len(commands)

    def run():
        pass

    def print_indexed_command_block(self):
        self.print_title_block("Your options are...", False, "|")
        for index, command in enumerate(self._commands, 1):
            print(TextFormatter.pad_text(f"{index} : {command}", self._line_width, "|"))
        print("|" * self._line_width)

    def get_command_block_choice(self):
        return self._get_integer_input(self._start, self._limit)

    def print_indexed_array_block(self, array):
        self.print_title_block("Your options are...", False, "|")
        for index, item in enumerate(array, 1):
            print(TextFormatter.pad_text(f"{index} : {item}", self._line_width, "|"))
        print("|" * self._line_width)

    def get_array_block_choice(self, start, limit):
        return self._get_integer_input(start, limit)

    def get_user_text_input(self, message=""):
        if message:
            self.print_title_block(message)
        return input()

    def print_title_block(self, title, end_space=True, end_character="*"):
        title_length = len(title)
        if title_length <= self._line_width - 4:
            print(end_character * self._line_width)
            print(
                TextFormatter.center_pad_text(
                    title.upper(), self._line_width, end_character
                )
            )
        else:
            split_titles = TextFormatter.split_oversized_text(
                title, self._line_width, end_character
            )
            print(end_character * self._line_width)

            for short_title in split_titles:
                print(
                    TextFormatter.center_pad_text(
                        short_title.upper(), self._line_width, end_character
                    )
                )

        print(end_character * self._line_width)

        if end_space:
            print()

    def print_text_block(self, text, end_space=True, end_character="*"):
        split_text = TextFormatter.split_oversized_text(text, self._line_width)
        print(end_character * self._line_width)
        for short_title in split_text:
            print(TextFormatter.pad_text(short_title, self._line_width))
        print(end_character * self._line_width)

        if end_space:
            print()

    def _get_integer_input(self, start, limit):
        print(
            TextFormatter.pad_text(
                f"Please enter a number between {start} - {limit}",
                self._line_width,
                "|",
            ),
        )

        try:
            user_input = int(input())
            if user_input not in range(start, limit + 1):
                print("Input out of range")
                return self._get_integer_input(start, limit)
            else:
                return user_input

        except ValueError:
            print("Incorrect input")
            return self._get_integer_input(start, limit)
