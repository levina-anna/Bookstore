from dotenv import load_dotenv
from decouple import config

load_dotenv()

api_domain = config('API_DOMAIN', default='http://127.0.0.1:8002')
debug = True if config('DEBUG', default="False") in ["true", "True"] else False
