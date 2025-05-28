from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
import requests
from dotenv import load_dotenv
import os

from .forms import AddPostForm


def give_forecast(request):
    load_dotenv()  # Загружает переменные из .env
    forecast_key = os.getenv('forecast_key')

    city = request.POST.get("city")
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={forecast_key}&units=metric&lang=ru"

    response = requests.get(url)
    data = response.json()
    if data.get("cod") != "200":
        return "Ошибка получения прогноза"
    
    forecast = []
    for item in data['list'][:4]:  # Ближайшие 12 часов (каждые 3 часа)
        time = datetime.strptime(item['dt_txt'], "%Y-%m-%d %H:%M:%S").strftime("%H:%M")
        temp = item['main']['temp']
        desc = item['weather'][0]['description']
        icon_code = item['weather'][0]['icon']
        forecast.append({"time": time, "temp": f"{temp}°C", "desc": desc, "icon_url": f"https://openweathermap.org/img/wn/{icon_code}@2x.png"})
    return forecast


def addpage(request):
    forecast= "В каком городе вы хотите узнать погоду?"
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            forecast = give_forecast(request)
    else:
        form = AddPostForm()
 
    return render(request, 'forecast/main.html', {'title': 'Добавление статьи', 'form': form, 'forecast': forecast})
