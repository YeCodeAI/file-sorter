from file_sorter.core import JSONDB


class DBCommands:
    def __init__(self):
        self.db = JSONDB()

    def get_all_command(self) -> None:
        self.db.get_all()

    def add_item(self, format: str, path: str) -> None:
        self.db.add_item(format, path)

    def remove_item(self, name_item: str) -> None:
        self.db.remove_item(name_item)
