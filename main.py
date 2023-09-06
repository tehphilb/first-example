import flet as ft
from Data.create_dummy_data import CreateDummyData
from Data.data_handler import DataHandler
from View.filter_row import FilterRow

from View.navbar import NavBar

"""get date from data_handler"""
data_generator = CreateDummyData(num_rows=50)  # Create a data generator
data_handler = DataHandler(data_generator)  # Retrieve the prepared data

# get data
data = data_handler.get_data()

# get list of unique continents
continents = data_handler.get_unique_continents()

# get list of unique countries
countries = data_handler.get_unique_countries()

# Create an instance of FilterRow
filter_row = FilterRow(
    continents=continents,
    countries=countries,
    data=data,
)


def main(page: ft.Page):
    ## page layout
    title = str("Flet example")
    page.title = title
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    ## navigation bar
    page.appbar = NavBar(page, title).create_appbar()

    ## main content
    page.add(
        ft.ResponsiveRow(
            controls=[
                filter_row.create_row(),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
    )


ft.app(
    target=main,
)
