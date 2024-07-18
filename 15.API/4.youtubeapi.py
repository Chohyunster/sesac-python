import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('YOUTUBE_API_KEY')

url = 'https://www.googleapis.com/youtube/v3/search'

search_query = 'Python programming'

params = {
    'part' : 'snippet',
    'q' : search_query,
    'type' : 'video',
    'maxResults' : 10,
    'key' : API_KEY,
}
#요청 및 결과 받아오기
response = requests.get(url, params)
response.raise_for_status()
data = response.json()
# print(data)

#필요한 데이터 가공
for item in data['items']:
    title = item['snippet']['title']
    video_id = item['id']['videoId']
    video_url = f'https://www.youtube.com/watch?v={video_id}'
    description = item['snippet']['description']
    print(f'제목: ', {title})
    print(f'제목: ', {video_url})
    print(f'제목: ', {description})
    print('-'*40)
