import requests
from utils.countries import get_biggest_countries_in_region


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
    biggest_countries_json = get_biggest_countries_in_region(region=all_region_countries_json, how_many_countries=10)
    return biggest_countries_json
