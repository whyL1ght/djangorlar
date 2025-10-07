# Project modules
from decouple import config

# ----------------------------------------------
# Env id
#
ENV_POSSIBLE_OPTIONS = [
    "local",
    "prod",
]

ENV_ID = config("PRACTICE-4_ENV_ID", cast=str)
SECRET_KEY = 'django-insecure-#k2sp!*g3ju9jla=-*2=zxa4$&ct(do!a=vvozh6#cxtscif_$'
