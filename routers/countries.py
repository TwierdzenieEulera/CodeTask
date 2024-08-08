from services import countries_service

from fastapi import APIRouter

router = APIRouter()


@router.get("/name/{country}", tags=["countries"])
async def get_country(country: str):
    return countries_service.get_country_data(country=country)


@router.get("/region/{region}", tags=["countries"])
async def get_region_biggest_countries(region: str):
    """
    Gets a json containing Country Name, Capital, Region, Sub Region, Population, Area, Borders
    :param region:
    :return: json
    """
    return countries_service.get_region_biggest_countries(region=region)


@router.get("/subregion/{subregion}", tags=["countries"])
async def get_subregion_countries_with_neighbours(subregion: str):
    """
    Gets a json containing Country Name, Capital, Region, Sub Region, Population, Area, Borders of country with
    neighbours
    :param subregion:
    :return: json
    """
    return countries_service.get_subregion_countries_with_neighbours(subregion=subregion)
