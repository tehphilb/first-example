class DataHandler:
    def __init__(self, data_generator):
        self.data_generator = data_generator
        self.df = self.prepare_data()

    def prepare_data(self):
        # Get the data from the provided data generator
        data = self.data_generator.get_data()
        return data

    def get_data(self):
        return self.df
    
    def get_unique_countries(self) -> list[str]:
        unique_countries = self.df['Country'].unique()
        return list(unique_countries)
    
    def get_unique_continents(self) -> list[str]:
        # Get unique continents from the DataFrame
        unique_continents = self.df['Continent'].unique()
        return list(unique_continents)        