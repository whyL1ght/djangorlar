# Python modules
from decouple import config

# ----------------------------------------------
# Env id
#
ENV_POSSIBLE_OPTIONS = (
    'local',
    'prod',
)

ENV_ID = config("PRACTICE-5_ENV_ID", cast=str)
SECRET_KEY = 'django-insecure--$ypsv^a=lojc6#mm%h5&y&f&9fi0shqynxu&rf*aerf3y$58v'
