import requests
from utils.countries import get_countries_with_neighbours, get_biggest_countries_in_region


def get_country_data(country: str):
    value = requests.get(f"https://restcountries.com/v3.1/name/{country}")
    return value.json()


def get_region_biggest_countries(region: str):
    """
    Returns list of dictionaries of biggest countries in given region
    :param region:
    :return:
    """
    all_region_countries = requests.get(f"https://restcountries.com/v3.1/region/{region}?fields="
                                        f"name,capital,region,subregion,population,area,borders")
    all_region_countries_json = all_region_countries.json()
    biggest_countries_json = get_biggest_countries_in_region(region=all_region_countries_json,
                                                             how_many_countries=10)
    return biggest_countries_json


def get_subregion_countries_with_neighbours(subregion: str):
    """
    Returns list of dictionaries of country with neighbours
    :param subregion:
    :return:
    """
    all_subregion_countries = requests.get(f"https://restcountries.com/v3.1/subregion/{subregion}?fields="
                                           f"name,capital,region,subregion,population,area,borders")
    all_subregion_countries_json = all_subregion_countries.json()
    countries_with_neighbours_json = get_countries_with_neighbours(subregion=all_subregion_countries_json,
                                                                   at_least_neighbours=4)
    return countries_with_neighbours_json
