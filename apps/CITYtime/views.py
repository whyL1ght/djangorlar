# Python modules
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
# Django modules
from django.shortcuts import render

def city_time(request):
    city = request.GET.get("city", "UTC")
    cities = {
        "Almaty": "Asia/Almaty",
        "Calgary": "America/Edmonton",
        "Moscow": "Europe/Moscow",
        "UTC": "UTC"
    }
    tz = ZoneInfo(cities.get(city, "UTC"))
    current_time = datetime.now(ZoneInfo(cities.get(city, "UTC"))).strftime("%Y-%m-%d %H:%M:%S")
    return render(
        request,
        "CITYtime/index.html",
        {"cities": cities.keys(), "city": city, "time": current_time}
    )


