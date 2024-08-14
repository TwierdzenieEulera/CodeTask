import json
import os
import tempfile

import pandas as pd
from fastapi import HTTPException
from fastapi.responses import FileResponse
from starlette.background import BackgroundTask
from app.utils.constans import Formats


def get_biggest_countries_in_region(region: list, how_many_countries: int) -> list:
    sorted_countries = sorted(region, key=lambda d: d['area'])[-how_many_countries-1:-1]
    return sorted_countries


def get_countries_with_neighbours(subregion: list, at_least_neighbours: int):
    countries_with_neighbours = []
    for country in subregion:
        if "borders" not in country:
            continue
        if len(country['borders']) >= at_least_neighbours:
            countries_with_neighbours.append(country)
    if not countries_with_neighbours:
        raise HTTPException(status_code=404, detail=f"No countries with more than {at_least_neighbours}"
                                                    f" borders found in this subregion")
    return countries_with_neighbours


def return_data_file(json_response, temp_format):
    if temp_format == Formats.JSON:
        fd, path = tempfile.mkstemp(suffix=f'.{temp_format}')
        json_object = json.dumps(json_response)
        with os.fdopen(fd, mode='w') as f:
            f.write(json_object)
        return FileResponse(path, media_type="application/json", background=BackgroundTask(os.remove, path))
    elif temp_format == Formats.CSV:
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            pd.DataFrame(json_response).to_csv(path_or_buf=temp.name + '.csv')
            temp.close()
        return FileResponse(temp.name + '.csv',
                            media_type="text/csv",
                            background=BackgroundTask(os.remove, temp.name + '.csv'))


def add_total_subregion_population(json_response: list):
    total_population = 0
    for country in json_response:
        total_population += country["population"]
    json_response.insert(0, {"total_population": total_population})
    return json_response
