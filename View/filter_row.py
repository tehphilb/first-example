import flet as ft

class FilterRow:
    def __init__(self, continents, countries, data):
        self.continents = continents
        self.countries = countries
        self.data = data

    def on_change(self, e):
        # access the event value (e) like this
        selected_continent = e.control.value
        return selected_continent

    def create_row(self):
        return ft.Row(
            controls=[
                ft.Dropdown(
                    on_change=self.on_change,
                    options=[ft.dropdown.Option(item) for item in self.continents],
                    label="Select a continent",
                    col={'md': 4},
                ),
                ft.Dropdown(
                    options=self.update_country_options(self.on_change),
                    label="Select a continent",
                    col={'md': 4},
                ),

            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
