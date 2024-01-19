from django.db import models


class WeatherData(models.Model):
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    date = models.DateTimeField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    feels_like = models.DecimalField(max_digits=5, decimal_places=2)
    temp_min = models.DecimalField(max_digits=5, decimal_places=2)
    temp_max = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    weather = models.CharField(max_length=255)
    air_quality = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"Weather data for {self.city} on {self.date}"


AirQuality = {
    1: 'Good',
    2: 'Fair',
    3: 'Moderate',
    4: 'Poor',
    5: 'Very Poor',
}
