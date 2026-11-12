from file_sorter.core import FileSort


def sorter_command(path: str) -> None:
    sorter = FileSort(path)

    sorter.sorter()
