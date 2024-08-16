import unittest
import requests
import json
import os

from fastapi import HTTPException
from app.utils.constans import region_list, Formats
from app.utils.countries import add_total_subregion_population, get_biggest_countries_in_region
from app.services.countries_service import (get_region_biggest_countries, get_countries_with_neighbours,
                                            get_subregion_countries_with_neighbours, get_subregion_population, )

BASE_URL = "https://restcountries.com/#rest-countries"


class TestApi(unittest.TestCase):

    def test_get_endpoint(self):
        response = requests.get(BASE_URL)
        self.assertEqual(response.status_code, 200)

    def test_get_biggest_countries_from_not_existing_region(self):
        try:
            get_region_biggest_countries(region="Spock",
                                         response_format=Formats.JSON)
        except HTTPException as e:
            self.assertEqual(e.status_code, 400)

    def test_get_countries_from_not_existing_subregion(self):
        try:
            get_subregion_countries_with_neighbours(subregion="Kirk",
                                                    response_format=Formats.JSON,
                                                    at_least_neighbours=1)
        except HTTPException as e:
            self.assertEqual(e.status_code, 400)

    def test_get_population_from_not_existing_subregion(self):
        try:
            get_subregion_population(subregion="Bones",
                                     response_format=Formats.JSON)
        except HTTPException as e:
            self.assertEqual(e.status_code, 400)

    def test_can_filter_biggest_countries(self):
        for region in region_list:
            response = self.get_file_path(f"test_data\\regions\\{region}.json")
            with open(response, "r", encoding="utf-8") as data:
                json_response = json.load(data)
            test_data = get_biggest_countries_in_region(region=json_response, how_many_countries=10)
            self.assertLessEqual(len(test_data), 10)
            test_list = [country["area"] for country in test_data]
            for idx in range(1, len(test_list)):
                self.assertLess(test_list[idx - 1], test_list[idx], "Countries are in wrong order")

    def test_get_countries_with_to_many_neighbours(self):
        file_path = self.get_file_path("test_data/southern_europe.json")
        with open(file_path, encoding="utf8") as f:
            test_data = json.load(f)
        try:
            get_countries_with_neighbours(subregion=test_data,
                                          at_least_neighbours=999)
        except HTTPException as e:
            self.assertEqual(e.status_code, 404)

    def test_add_total_subregion_population(self):
        json_response = [
            {"name": "Country Enterprise", "population": 5000000},
            {"name": "Country Deep State 9", "population": 10000000},
            {"name": "Country Voyager", "population": 7500000}
        ]

        expected_output = [
            {"total_population": 22500000},
            {"name": "Country Enterprise", "population": 5000000},
            {"name": "Country Deep State 9", "population": 10000000},
            {"name": "Country Voyager", "population": 7500000}
        ]
        result = add_total_subregion_population(json_response)
        self.assertEqual(result, expected_output)

    def test_add_total_subregion_population_empty_json_response(self):
        json_response = []
        expected_output = [{"total_population": 0}]
        result = add_total_subregion_population(json_response)
        self.assertEqual(result, expected_output)

    def test_add_total_subregion_population_single_country(self):
        json_response = [{"name": "Country Enterprise", "population": 1000000}]
        expected_output = [
            {"total_population": 1000000},
            {"name": "Country Enterprise", "population": 1000000}
        ]
        result = add_total_subregion_population(json_response)
        self.assertEqual(result, expected_output)

    @staticmethod
    def get_file_path(relative_path):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_dir, relative_path)


if __name__ == '__main__':
    unittest.main()
