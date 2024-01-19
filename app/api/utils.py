import requests

from datetime import datetime

from config import API_KEY


def location_search(query: str) -> (float, float):
    """Finds latitude and longitude for a location

    Args:
        query (str): location query

    Returns:
        float, float: latitude and longitude
    """

    # TODO: show more results so the user can choose the rigth one
    #       returning the first result (the result the api judged to be the best fit)
    results_limit = 1
    result = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={query}&limit={results_limit}&appid={API_KEY}').json()

    if len(result) == 0:
        raise Exception('Location not finded')

    return result[0]


def validate_path_params(location, start_date, end_date):
    try:
        datetime.strptime(start_date, '%Y/%m/%d-%H:%M')
        datetime.strptime(end_date, '%Y/%m/%d-%H:%M')
    except (ValueError, TypeError):
        raise Exception('Invalid date format. Please use YYYY/MM/DD-HH:MM for startDate and endDate.')
