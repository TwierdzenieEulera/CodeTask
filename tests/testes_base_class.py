import unittest
import requests
import json
import os

from fastapi import HTTPException
from app.utils.constans import region_list, Formats
from app.services.countries_service import get_region_biggest_countries, get_countries_with_neighbours

BASE_URL = "https://restcountries.com/#rest-countries"


class TestApi(unittest.TestCase):

    def test_get_endpoint(self):
        response = requests.get(BASE_URL)
        assert response.status_code == 200

    def test_can_get_biggest_countries(self):
        for region in region_list:
            response = get_region_biggest_countries(region=region, response_format=Formats.JSON)
            print(response)
            with open(response.path, "r") as data:
                json_data = json.load(data)
                print(json_data)
                assert len(json_data) <= 10
                test_list = [country["area"] for country in json_data]
                for idx in range(1, len(test_list)):
                    if test_list[idx - 1] < test_list[idx]:
                        continue
                    else:
                        raise ValueError("Countries are in wrong order")

    def test_get_countries_with_to_many_neighbours(self):
        file_path = self.get_file_path("test_data/southern_europe.json")
        with open(file_path, encoding="utf8") as f:
            test_data = json.load(f)
        try:
            get_countries_with_neighbours(subregion=test_data,
                                          at_least_neighbours=999)
        except HTTPException as e:
            assert e.status_code == 404

    @staticmethod
    def get_file_path(relative_path):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_dir, relative_path)


if __name__ == '__main__':
    unittest.main()
