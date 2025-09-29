# Django modules
from django.contrib import admin
from django.urls import include, path

# Project modules
from apps.home import urls as home_urls
from apps.users import urls as users_urls
from apps.CITYtime import urls as citytime_urls
from apps.cnt import urls as cnt_urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_urls)),
    path('users/', include(users_urls)),
    path('city-time/', include(citytime_urls)),
    path('cnt/', include(cnt_urls)),
]
