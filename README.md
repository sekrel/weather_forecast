<<<<<<< HEAD
# Прогноз погоды с использованием OpenWeatherMap API

## Требования для запуска проекта
- скачать DockerFile
- API-ключ от [OpenWeatherMap](https://openweathermap.org/)
- SECRET_KEY= "ключ django"

## Запуск приложения с помощью DockerFile командами
docker build . -f DockerFile -t django_project
docker run -e SECRET_KEY="ключ django" -e forecast_key="ключ api openweathermap" -p 8000:8000 -t django_project   
=======
для работы нужен файл .env c ключами
SECRET_KEY= "ключ django"
forecast_key = "ключ api openweathermap"
>>>>>>> 1d379718998e34594ecf49af1c04fa0462fa83b3
