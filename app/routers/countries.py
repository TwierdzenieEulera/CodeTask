from app.services import countries_service
from fastapi import APIRouter, Path, Query
from app.utils.constans import Formats

router = APIRouter()


@router.get("/region/{region}", tags=["countries"])
async def get_region_biggest_countries(region: str = Path(example="Europe"),
                                       how_many_countries: int = Path(example=10),
                                       response_format: Formats = Query(example=Formats.JSON)):
    """
    Gets a data containing Country Name, Capital, Region, Sub Region, Population, Area, Borders
    ```
    :param str region: region of the world (Europe, Asia, Oceania, Americas, etc.)
    :param int how_many_countries: determine maximum number of countries that will be sorted
    :param str response_format: choose JSON or CSV as output formats
    :return: json or csv, depending on chosen response format
    ```
    """
    return countries_service.get_region_biggest_countries(region=region,
                                                          how_many_countries=how_many_countries,
                                                          response_format=response_format)


@router.get("/subregion/{subregion}", tags=["countries"])
async def get_subregion_countries_with_neighbours(subregion: str = Path(example="Southern Europe"),
                                                  at_least_neighbours: int = Query(example=4),
                                                  response_format: Formats = Query(example=Formats.JSON)):
    """
    Gets a data containing Country Name, Capital, Region, Sub Region, Population, Area, Borders of country with
    neighbours
    ```
    :param str subregion: subregion of the world (South America, West Europe,  Eastern Asia, etc.)
    :param int at_least_neighbours: minimal number of neighbours to be counted in response
    :param str response_format: choose JSON or CSV as output formats
    :return: json or csv, depending on chosen response format
    ```
    """
    return countries_service.get_subregion_countries_with_neighbours(subregion=subregion,
                                                                     at_least_neighbours=at_least_neighbours,
                                                                     response_format=response_format)


@router.get("/subregion/population/{subregion}", tags=["countries"])
async def get_subregion_population(subregion: str = Path(example="Southern Europe"),
                                   response_format: Formats = Query(example=Formats.JSON)):
    """
    Gets a data containing total population of subregion and countries names from it
    ```
    :param str subregion: subregion of the world (South America, West Europe,  Eastern Asia, etc.)
    :param str response_format: choose JSON or CSV as output formats
    :return: json or csv, depending on chosen response format
    ```
    """
    return countries_service.get_subregion_population(subregion=subregion,
                                                      response_format=response_format)
