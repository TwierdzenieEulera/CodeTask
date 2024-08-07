import requests


def get_country_data(country: str):
    value = requests.get(f"https://restcountries.com/v3.1/name/{country}")
    return value.json()
