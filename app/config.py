import os
from dotenv import load_dotenv
from os.path import join, dirname, isfile

# Verify if .env exists
if isfile(r'./.env'):
    # Setting .env variables
    env_path = join(dirname(__file__), r'./.env')
    load_dotenv(env_path)
    print(" * Environment [Dev]")
else:
    print(" * Environment [QA/PROD]")

API_KEY = os.environ['API_KEY']
