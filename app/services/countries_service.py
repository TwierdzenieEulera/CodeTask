import requests
from app.utils.constans import region_list, sub_region_list, Formats
from app.utils.countries import (get_countries_with_neighbours, get_biggest_countries_in_region, return_data_file,
                                 add_total_subregion_population)
from fastapi import HTTPException

BASE_URL = "https://restcountries.com/v3.1"


def get_region_biggest_countries(region: str, how_many_countries: int, response_format: Formats):
    """
    Returns data of biggest countries in given region
    :param region:
    :param how_many_countries:
    :param response_format:
    :return:
    """
    if region in region_list:
        all_region_countries = requests.get(f"{BASE_URL}/region/{region}?fields="
                                            f"name,capital,region,subregion,population,area,borders")
        all_region_countries_json = all_region_countries.json()
        biggest_countries_json = get_biggest_countries_in_region(region=all_region_countries_json,
                                                                 how_many_countries=how_many_countries)
        return return_data_file(biggest_countries_json, temp_format=response_format)
    else:
        raise HTTPException(status_code=400, detail=f"Region {region} doesn't exist. "
                                                    f"Please use region from list {region_list}")


def get_subregion_countries_with_neighbours(subregion: str, at_least_neighbours: int, response_format: Formats):
    """
    Returns data of country with neighbours
    :param subregion:
    :param at_least_neighbours:
    :param response_format:
    :return:
    """
    if subregion in sub_region_list:
        all_subregion_countries = requests.get(f"{BASE_URL}/subregion/{subregion}?fields="
                                               f"name,capital,region,subregion,population,area,borders")
        all_subregion_countries_json = all_subregion_countries.json()
        countries_with_neighbours_json = get_countries_with_neighbours(subregion=all_subregion_countries_json,
                                                                       at_least_neighbours=at_least_neighbours)

        return return_data_file(countries_with_neighbours_json, temp_format=response_format)
    else:
        raise HTTPException(status_code=400, detail=f"Subregion {subregion} doesn't exist. "
                                                    f"Please use existing subregion from list {sub_region_list}")


def get_subregion_population(subregion: str, response_format: Formats):
    """
    Returns data containing total population of subregion and countries names from it
    :param subregion:
    :param response_format:
    :return:
    """
    if subregion in sub_region_list:
        all_subregion_countries = requests.get(f"{BASE_URL}/subregion/{subregion}?fields="
                                               f"name,population")
        all_subregion_countries_json = all_subregion_countries.json()
        subregion_data_plus_total_population = add_total_subregion_population(all_subregion_countries_json)

        return return_data_file(subregion_data_plus_total_population, temp_format=response_format)
    else:
        raise HTTPException(status_code=400, detail=f"Subregion {subregion} doesn't exist. "
                                                    f"Please use existing subregion from list {sub_region_list}")
