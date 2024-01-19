# Take Home - Django Project

## This project
The goal of this project is to create an API that assists users in planning their travels by offering accurate and up-to-date weather forecasts for specific locations and dates. 

## Features

- Get forecast weather conditions for a specific location between specific dates.
- Search the forecasted weather condicions and save it into database to faster access.

## API Endpoints

/api/v1/weather/search

With the `/search` endpoint you can get the forecasted weather data and save on the database, so you can get it later using the `/get` endpoint.

/api/v1/weather/get

With the `/get` endpoint you can search for saved data about the forecast weather.

Both with the following path params:
```
location, startDate and endDate
```

For example:
```
/api/v1/weather/search?location=London&startDate=2024/01/20-14:00&endDate=2024/01/21-21:00
```

## Getting Started
Dependencies:
* Docker - See [Get Docker](https://docs.docker.com/get-docker/)
* Docker Compose - Installed with Docker Desktop, See [Install Docker Compose](https://docs.docker.com/compose/install/)
* [OpenWeather API](https://openweathermap.org/api): Utilized for weather data.

First, set up your OpenWeather API key by following the [OpenWeather API documentation](https://openweathermap.org/appid).

Create a .env file (e.g., `.env-example`) with your OpenWeather API key.

With the dependencies installed, running the project is as simple as running:
```bash
docker compose up
```

This will pull the required Docker images and spin up a container running your service on http://localhost:8000.

To end the service, press `Ctrl+C`
