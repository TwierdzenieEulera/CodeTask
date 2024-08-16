# CodeTask

This is a simple FastAPI project to consume the [RESTCountries](https://restcountries.com/) API.

# Installation

run command 

    pip install --no-cache-dir --upgrade -r requirements.txt

Then to run the project you can run

    uvicorn app.main:app --host 127.0.0.1 --port 80

and open address [CT_API](http://127.0.0.1/docs) in your browser.

You can also use docker image. Just install docker and use commands:

    docker build -t fastapi-docker-image . 
    docker run -dp 8080:80 fastapi-docker-image

# Description

Web API consumes data from a public API and exposes endpoints with the following data:

    1. List the 10 biggest countries of a determined region of the world (Europe, Asia, Oceania, Americas, etc).
    2. List all the countries of a determined subregion (South America, West Europe,  Eastern Asia, etc) that has borders with more than 3 countries.
    3. List the population of a subregion, including the countries that are part of it.

Features:

    1. All endpoints support JSON and CSV as output formats.
    2. The code is partially covered by tests.
    3. The country data response object (used in points 1 and 2), contain the following data:
        Country Name
        Capital
        Region
        Sub Region
        Population
        Area
        Borders
    4. Response object for endpoint 3 is just a wrapper of the country name, plus the total population of the subregion.
    5. The application is available as a service in a container image.
    6. Documentation with instructions on how to run the application, what are the parameters used in the endpoints.


Data source:

    https://restcountries.com/

