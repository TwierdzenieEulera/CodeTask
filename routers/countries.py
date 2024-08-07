from services import countries_service

from fastapi import APIRouter

router = APIRouter()


@router.get("/countries/{country}")
async def get_country(country: str):
    return countries_service.get_country_data(country=country)
