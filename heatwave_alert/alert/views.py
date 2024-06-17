from django.http import JsonResponse, HttpResponse
from .models import Subscriber
import joblib
import requests
from twilio.rest import Client
import logging

model = joblib.load('heat_wave_predictor.joblib')
scaler = joblib.load('scaler.joblib')
API_KEY = ''
BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast'
TWILIO_ACCOUNT_SID = ''
TWILIO_AUTH_TOKEN = ''
TWILIO_PHONE_NUMBER = ''
def get_weather_data(lat, lon):
    params = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return {
        'temp': data['list'][0]['main']['temp'],
        'humidity': data['list'][0]['main']['humidity'],
        'wind_speed': data['list'][0]['wind']['speed']
    }
def check_heat_wave(request):
    subscribers = Subscriber.objects.all()
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    for subscriber in subscribers:
        weather_data = get_weather_data(subscriber.latitude, subscriber.longitude)
        features = [[weather_data['temp'], weather_data['humidity'], weather_data['wind_speed']]]
        features_scaled = scaler.transform(features)
        predicted_temp = model.predict(features_scaled)[0]
        if predicted_temp > 37:
            message = f"Alert! Heat wave expected with temperature {predicted_temp}°C."
            try:
                message_response = client.messages.create(
                    to=subscriber.phone_number,
                    from_=TWILIO_PHONE_NUMBER,
                    body=message
                )
                logger.info(f"Sent message to {subscriber.phone_number}: {message}")
                logger.info(f"Twilio response: {message_response.sid}")
            except Exception as e:
                logger.error(f"Error sending SMS to {subscriber.phone_number}: {e}")
        if request.path.startswith('/admin/'):
            return HttpResponse("Heat wave alerts have been sent.")
        else:
            return JsonResponse({'status': 'alerts sent'})
# Replace 'your_twilio_account_sid', 'your_twilio_auth_token', and 'your_twilio_phone_number' with your actual Twilio credentials.
