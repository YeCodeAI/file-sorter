import pathlib

from tinydb import Query, TinyDB

from file_sorter.ui import UI


class JSONDB:
    def __init__(self):
        self.home = pathlib.Path().home() / '.file-sorter'
        self.home.mkdir(parents=True, exist_ok=True)

        self.full_path = self.home / 'formats.json'

        self.db = TinyDB(self.full_path)
        self.ui = UI()

    def add_item(self, format: str, path_dir: str) -> None:
        """
        Add item in DB

        :param str format: File format
        :param str path_dir: The folder where files of this format are located
        """
        name = format.strip('.').upper()

        pathlib.Path(path_dir).mkdir(parents=True, exist_ok=True)
        self.ui.log(f'Folder successfully created at path: {path_dir}')

        self.ui.info('Saving to database...')
        self.db.insert({'name': name, 'format': format, 'path': path_dir})

        self.ui.success('Data successfully saved!')

    def get_all(self) -> None:
        """Retrieving all data from the database and displaying it in a table"""
        items = self.db.all()

        self.ui.create_tables(items)

    def remove_item(self, name_item: str) -> None:
        """
        Method for removing an item by name

        :param str name_item: Name item
        """
        Format = Query()
        name = name_item.strip('.').upper()
        data = self.db.search(Format.name == name)

        if not data:
            self.ui.warning(f'Name "{name_item}" does not exist!')
        else:
            self.db.remove(Format.name == name)
            self.ui.success(f'Format "{name_item}" successfully deleted!')
