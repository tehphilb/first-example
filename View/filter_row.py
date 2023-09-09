import flet as ft


class FilterRow(ft.UserControl):
    def __init__(self, continents, data):
        super().__init__()
        self.continents = continents
        self.data = data

    def build(self):
        self.continent_dd = ft.Dropdown(
            on_change=self.on_change,
            options=[ft.dropdown.Option(item) for item in self.continents],
            label="Select a continent",
            col={"md": 4},
        )

        self.country_dd = ft.Dropdown(
            options=[ft.dropdown.Option("Select a continent first")],
            label="Select a country",
            col={"md": 4},
        )

        return ft.Row(
            controls=[
                self.continent_dd,
                self.country_dd,
            ],
        )

    def on_change(self, e):
        selected_continent = e.control.value
        filtered_data = self.data[self.data["Continent"] == selected_continent]
        unique_countries = filtered_data["Country"].unique()

        # Update the options of the dropdown and trigger a refresh
        self.country_dd.options = [
            ft.dropdown.Option(item) for item in unique_countries
        ]
        self.update()
