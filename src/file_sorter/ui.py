from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


class UI:
    def success(self, text: str) -> None:
        console.print(f'[green][+] {text}[/green]')

    def warning(self, text: str) -> None:
        console.print(f'[yellow][!] {text}[/yellow]')

    def error(self, text: str) -> None:
        console.print(f'[red][-] {text}[/red]')

    def info(self, text: str) -> None:
        console.print(f'[cyan][*] {text}[/cyan]')

    def log(self, text: str) -> None:
        console.log(text)

    def create_panel(self, text: str, title: str) -> None:
        panel = Panel(text, title=title, title_align='center', expand=False)

        console.print(panel)

    def create_tables(self, items: list) -> None:
        table = Table(title='All registred formats', border_style='green')

        table.add_column('Name', style='cyan')
        table.add_column('Format', style='cyan')
        table.add_column('Path', style='cyan')

        for item in items:
            name = item.get('name')
            format = item.get('format')
            path = item.get('path')

            table.add_row(name, format, path)

        console.print(table)
