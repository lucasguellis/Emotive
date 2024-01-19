import json

from django.http import JsonResponse

from .service import WeatherService
from .utils import validate_path_params


def search(req):
    location = req.GET.get('location', None)
    start_date = req.GET.get('startDate', None)
    end_date = req.GET.get('endDate', None)

    if not all([location, start_date, end_date]):
        return JsonResponse({'error': 'You must enter location, startDate and endDate to see the weather'}, status=500)

    try:
        weather_service = WeatherService(location)
        validate_path_params(location, start_date, end_date)

        # Returns data from weather API and saves it on the database
        weather_data = weather_service.request_weather_data()
        air_quality_data = weather_service.request_air_pollution_quality()

        weather_service.save_weather_data(weather_data, air_quality_data)

        return get(req)

    except Exception as error:
        return JsonResponse({'error': str(error)})


def get(req):
    location = req.GET.get('location', None)
    start_date = req.GET.get('startDate', None)
    end_date = req.GET.get('endDate', None)

    if not all([location, start_date, end_date]):
        return JsonResponse({'error': 'You must enter location, startDate and endDate to see the weather'}, status=500)

    try:
        validate_path_params(location, start_date, end_date)
        weather_service = WeatherService(location)

        # Retrieves data if it alreary exists on database
        data = weather_service.get_weather_data(start_date, end_date)
        parsed_data = json.loads(data)

        return JsonResponse(parsed_data, safe=False)

    except Exception as error:
        return JsonResponse({'error': str(error)})
