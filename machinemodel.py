import requests 
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

API_KEY = ''
BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast'  
def get_weather(lat, lon, timestamp=None):
    params = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()
lat = 40.7128
lon = -74.0060
weather_data = get_weather(51.5074, -0.1278)
print(weather_data)
weather_data = get_weather(51.5074, -0.1278, 1655136000)
print(weather_data)
df = pd.json_normalize(weather_data['list'])
df['heat_wave'] = df['main.temp'] > 35  
features = ['main.temp', 'main.humidity', 'wind.speed']
X = df[features]
y = df['heat_wave']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
joblib.dump(model, 'heat_wave_predictor.joblib')
joblib.dump(scaler, 'scaler.joblib')
