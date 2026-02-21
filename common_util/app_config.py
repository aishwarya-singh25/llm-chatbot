"""
App config and supported functions
"""

import os
import requests

env = os.getenv("ENV", "default")
sessions = requests.Session()


def load_data():
    """Loads data from config server"""
    return None