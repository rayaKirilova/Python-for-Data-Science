countries = [country for country in input().split(', ')]
capitals = [capital for capital in input().split(', ')]

country_capital_dictionary = {country: capital for country, capital in zip(countries, capitals)}

for country, capital in country_capital_dictionary.items():
    print(f'{country} -> {capital}')