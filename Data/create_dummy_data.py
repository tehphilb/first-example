import pandas as pd
import random
from countryinfo import CountryInfo

class CreateDummyData:
    def __init__(self, num_rows=1000):
        self.num_rows = num_rows
        self.df = self.generate_data()

    def generate_data(self) -> pd.DataFrame:
        # Get a list of all available countries
        all_countries = list(CountryInfo().all().keys())

        # Create an empty DataFrame
        df = pd.DataFrame(columns=['Country', 'Continent', 'Serial Number'])

        # Generate random data and add it to the DataFrame
        for _ in range(self.num_rows):
            # Randomly select a country
            country = random.choice(all_countries)

             # Get the continent for the selected country if available, otherwise assign NaN
            try:
                continent = CountryInfo(country).region()
            except KeyError:
                continent = float('nan')

            # Generate a random six-digit serial number
            serial_number = random.randint(100000, 999999)

            # Create a new DataFrame for the current row
            new_row = pd.DataFrame({'Country': [country], 'Continent': [continent], 'Serial Number': [serial_number]})

            # Concatenate the new row to the existing DataFrame
            df = pd.concat([df, new_row], ignore_index=True)

        return df

    def get_data(self):
        return self.df

# Example usage:
if __name__ == "__main__":
    data_generator = CreateDummyData(num_rows=50)
    df = data_generator.get_data()
    print(df.head())
