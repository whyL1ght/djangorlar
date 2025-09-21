# Project modules
from decouple import config

# ----------------------------------------------
# Env id
#
ENV_POSSIBLE_OPTIONS = (
    "local",
    "prod",
)
ENV_ID = config("PRACT3_ENV_ID", cast=str)
SECRET_KEY = 'django-insecure-o58t&@a64bdb*q7ffby&)cwnkat2@mv5pch7q)as@)ctnfxxb-'