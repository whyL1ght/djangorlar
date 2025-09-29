# Project modules
from decouple import config

# ----------------------------------------------
# Env id
#
ENV_POSSIBLE_OPTIONS = (
    'local',
    'prod',
)

ENV_ID = config("PRACTICE-3_ENV_ID", cast=str)
SECRET_KEY = 'django-insecure--268rf5m)openk10c5(x&pnl!b8@$-#@_9t52su!61-c(w*s_='