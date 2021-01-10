import os

import json
from django.core.exceptions import ImproperlyConfigured

settings_file_path = os.getenv("NETWORK_COVERAGE_SETTINGS", "")
settings_file = json.load(open(settings_file_path))


def get_setting(name):
    if name not in settings_file:
        raise ImproperlyConfigured(f"Setting {name} isn't not in settings file: {settings_file_path}")
    return settings_file.get(name)
