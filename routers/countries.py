from services import countries_service
from fastapi import APIRouter

router = APIRouter()


@router.get("/name/{country}", tags=["countries"])
async def get_country(country: str):
    return countries_service.get_country_data(country=country)


@router.get("/region/{region}", tags=["countries"])
async def get_region_biggest_countries(region: str, response_format: str):
    """
    Gets a json containing Country Name, Capital, Region, Sub Region, Population, Area, Borders
    :param region:
    :param response_format:
    :return: json
    """
    return countries_service.get_region_biggest_countries(region=region,
                                                          response_format=response_format)


@router.get("/subregion/{subregion}", tags=["countries"])
async def get_subregion_countries_with_neighbours(subregion: str, response_format: str):
    """
    Gets a json containing Country Name, Capital, Region, Sub Region, Population, Area, Borders of country with
    neighbours
    :param subregion:
    :param response_format:
    :return: json
    """
    return countries_service.get_subregion_countries_with_neighbours(subregion=subregion,
                                                                     response_format=response_format)
