"""
Create base url for studio page objects.
While creating the url, basic authentication
username and basic authentication password
should be used.
"""

import os

from regression.pages import BASIC_AUTH_USERNAME, BASIC_AUTH_PASSWORD

STUDIO_STAGE_BASE_URL = os.environ.get('STUDIO_STAGE_BASE_URL','studio.stage.edx.org')

STUDIO_BASE_URL = os.environ.get('STUDIO_BASE_URL', STUDIO_STAGE_BASE_URL)

if BASIC_AUTH_PASSWORD == "not_set" or BASIC_AUTH_USERNAME == "not_set":
    LOGIN_BASE_URL = os.environ.get('STUDIO_LOGIN_BASE_URL','https://{}'.format(
        STUDIO_BASE_URL
        ))
else:
    LOGIN_BASE_URL = os.environ.get('STUDIO_LOGIN_BASE_URL','https://{}:{}@{}'.format(
            BASIC_AUTH_USERNAME, BASIC_AUTH_PASSWORD, STUDIO_BASE_URL
        ))

