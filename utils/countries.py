import json
import pandas as pd


def get_biggest_countries_in_region(region: list, how_many_countries: int) -> list:
    sorted_countries = sorted(region, key=lambda d: d['area'])[-how_many_countries:-1]
    return sorted_countries


def get_countries_with_neighbours(subregion: list, at_least_neighbours: int):
    countries_with_neighbours = []
    for country in subregion:
        if len(country['borders']) >= at_least_neighbours:
            countries_with_neighbours.append(country)
    return countries_with_neighbours


def convert_json_to_csv(file_json):
    with open(file_json) as json_file:
        json_data = json.load(json_file)

    csv_data = pd.DataFrame(json_data).to_csv('out.csv', index=False)

    return csv_data
