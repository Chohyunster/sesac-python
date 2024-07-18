import requests
from dotenv import load_dotenv
import os

#env 파일을 읽어서 메모리에 로딩한다.
load_dotenv()

OW_API_KEY = os.getenv('OPENWETHERMAP_API_KEY')

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    'q' : 'Seoul',
    'units' : 'metric',
    'appid': 'OW_API_KEY'
}

#요청 및 결과 받아오기
response = requests.get(url, params=params)
response.raise_for_status()
weather_data = response.json()

#필요한 데이터 가공
city_name = weather_data['name']
temperature = weather_data['main']['temp']
description = weather_data['weather'][0]['description']

print(f'도시: {city_name}')
print(f'온도: {temperature}')
print(f'날씨: {description}')