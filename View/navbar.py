import flet as ft


class NavBar:
    def __init__(self, page, title):
        self.page = page
        self.title = title

    def create_appbar(self):
        self.page.appbar = ft.AppBar(
            title=ft.Text(
                self.title,
                color=ft.colors.WHITE,
            ),
            bgcolor=ft.colors.PURPLE_900,
        )
        return self.page.appbar
