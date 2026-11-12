import pathlib
import shutil

from file_sorter.ui import UI

from .jsondb import JSONDB


class FileSort:
    def __init__(self, source_dir: str):
        self.source_dir = pathlib.Path(source_dir)
        self.db = JSONDB()
        self.ui = UI()

    def sorter(self) -> None:
        """A method for sorting files based on their formats"""

        if not self.source_dir.exists():
            self.ui.warning(f'Folder {self.source_dir} does not exist')
            return

        records = self.db.db.all()

        if not records:
            self.ui.warning('No registered formats for sorting found in the database!')
            return

        formats_maps = {}

        for item in records:
            fmt = item.get('format').lower()
            path = item.get('path')

            if fmt and path:
                formats_maps[fmt] = pathlib.Path(path)

        sorted_count = 0

        for file_path in self.source_dir.iterdir():
            if file_path.is_file():
                file_ext = file_path.suffix.lower()

                if file_ext in formats_maps:
                    target_dir = formats_maps[file_ext]

                    if target_dir.suffix:
                        target_folder = target_dir.parent
                    else:
                        target_folder = target_dir

                    target_folder.mkdir(parents=True, exist_ok=True)

                    dest_path = target_folder / file_path.name

                    shutil.move(str(file_path), str(dest_path))
                    self.ui.log(f'File "{file_path.name}" moved to "{target_folder}"')
                    sorted_count += 1

        if sorted_count > 0:
            self.ui.success(f'Sorting completed. Successfully moved files: {sorted_count}')
        else:
            self.ui.info('No files found matching the registered formats')
