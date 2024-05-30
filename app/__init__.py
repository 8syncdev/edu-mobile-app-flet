
#* Thiết lập config chung cho app
import flet as ft

#* Create directory cho app
import pathlib
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent


#* Base size of phone
PHONE_WIDTH = 400
PHONE_HEIGHT = 850


#* Load env
from dotenv import load_dotenv
import os
load_dotenv(BASE_DIR / '.env', override=True)
API_BE = os.getenv('API_BE')
DOMAIN_BE = os.getenv('DOMAIN_BE')
DOMAIN_API = f'{DOMAIN_BE}/{API_BE}'
SENTIMENT_API_DOMAIN = os.getenv('SENTIMENT_API_DOMAIN')
TURN_ON_SCREEN= os.getenv('TURN_ON_SCREEN')=='True'

