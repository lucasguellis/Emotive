import requests
import logging

from django.core import serializers
from datetime import datetime
from typing import List

from config import API_KEY
from .utils import location_search
from .models import WeatherData, AirQuality


class WeatherService:
    # TODO: alterar nome
    def __init__(self, location):
        self.location = location
        self.API_KEY = API_KEY

    @property
    def coordinates(self):
        location = location_search(self.location)
        return location['lat'], location['lon']

    @property
    def city_name(self):
        location = location_search(self.location)
        return location['name']

    @property
    def country_name(self):
        location = location_search(self.location)
        return location['country']

    @property
    def weather_api_url(self):
        lat, lon = self.coordinates
        return f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={self.API_KEY}&units=metric'

    @property
    def air_pollution_api_url(self):
        lat, lon = self.coordinates
        return f'http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={self.API_KEY}'

    def get_weather_data(self, start_date, end_date) -> List[dict]:
        # Retrieves weather data
        result = WeatherData.objects.filter(
            city=self.city_name,
            country=self.country_name,
            date__range=(
                datetime.strptime(start_date, '%Y/%m/%d-%H:%M').replace(tzinfo=None),
                datetime.strptime(end_date, '%Y/%m/%d-%H:%M').replace(tzinfo=None)
            ),
        ).all()
        return serializers.serialize("json", result)

    def request_weather_data(self) -> dict:
        # Requests weather data to weather API
        result = requests.get(self.weather_api_url).json()

        if result['cod'] != '200':
            logging.error('Error trying to get weather data from openweather')
            logging.error('result: ' + str(result))
            raise Exception('Something went wrong :( Please try again later.')

        return result

    def request_air_pollution_quality(self) -> dict:
        # Requests air polution data to weather API
        result = requests.get(self.air_pollution_api_url)

        if result.status_code != 200:
            logging.error('Error trying to get air pollution data from openweather')
            logging.error('result: ' + result.text)
            raise Exception('Something went wrong :( Please try again later.')

        return result.json()['list']

    def save_weather_data(self, forecasted_weather_data, forecasted_air_pollution_data):
        # Saves data to the database if it doesnt exist
        for data in forecasted_weather_data['list']:
            if WeatherData.objects.filter(
                city=self.city_name,
                country=forecasted_weather_data['city']['country'],
                date=datetime.fromtimestamp(data['dt']),
            ):
                continue

            air_quality = next(filter(lambda x: x['dt'] == data['dt'], forecasted_air_pollution_data), None)

            weather_data = WeatherData()
            weather_data.city = self.city_name
            weather_data.country = forecasted_weather_data['city']['country']
            weather_data.date = datetime.fromtimestamp(data['dt'])
            weather_data.temperature = data['main']['temp']
            weather_data.feels_like = data['main']['feels_like']
            weather_data.temp_min = data['main']['temp_min']
            weather_data.temp_max = data['main']['temp_max']
            weather_data.humidity = data['main']['humidity']
            weather_data.weather = data['weather'][0]['main']
            weather_data.air_quality = AirQuality[air_quality['main']['aqi']] if air_quality else None
            weather_data.save()
