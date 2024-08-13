import requests
from utils.countries import (get_countries_with_neighbours, get_biggest_countries_in_region, return_data_file,
                             add_total_subregion_population)
from fastapi import HTTPException


BASE_URL = "https://restcountries.com/v3.1"


def get_region_biggest_countries(region: str, response_format: str):
    """
    Returns data of biggest countries in given region
    :param region:
    :param response_format:
    :return:
    """
    if response_format in ["csv", "json"]:
        all_region_countries = requests.get(f"{BASE_URL}/region/{region}?fields="
                                            f"name,capital,region,subregion,population,area,borders")
        all_region_countries_json = all_region_countries.json()
        biggest_countries_json = get_biggest_countries_in_region(region=all_region_countries_json,
                                                                 how_many_countries=10)
        return return_data_file(biggest_countries_json, temp_format=response_format)
    else:
        raise HTTPException(status_code=400, detail=f"Unsupported format {response_format}. Please use csv or json")


def get_subregion_countries_with_neighbours(subregion: str, response_format: str):
    """
    Returns data of country with neighbours
    :param subregion:
    :param response_format:
    :return:
    """
    if response_format in ["csv", "json"]:
        all_subregion_countries = requests.get(f"{BASE_URL}/subregion/{subregion}?fields="
                                               f"name,capital,region,subregion,population,area,borders")
        all_subregion_countries_json = all_subregion_countries.json()
        countries_with_neighbours_json = get_countries_with_neighbours(subregion=all_subregion_countries_json,
                                                                       at_least_neighbours=4)

        return return_data_file(countries_with_neighbours_json, temp_format=response_format)
    else:
        raise HTTPException(status_code=400, detail=f"Unsupported format {response_format}. Please use csv or json")


def get_subregion_population(subregion: str, response_format: str):
    """
    Returns data of country with neighbours
    :param subregion:
    :param response_format:
    :return:
    """
    if response_format in ["csv", "json"]:
        all_subregion_countries = requests.get(f"{BASE_URL}/subregion/{subregion}?fields="
                                               f"name,population")
        all_subregion_countries_json = all_subregion_countries.json()
        subregion_data_plus_total_population = add_total_subregion_population(all_subregion_countries_json)

        return return_data_file(subregion_data_plus_total_population, temp_format=response_format)
    else:
        raise HTTPException(status_code=400, detail=f"Unsupported format {response_format}. Please use csv or json")
