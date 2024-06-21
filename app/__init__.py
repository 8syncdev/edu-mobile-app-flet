'''
    Author: Nguyễn Phương Anh Tú
    
    The main purpose of this code is to configure the app by setting up directory paths, defining base sizes for a phone UI, and loading environment variables from a .env file.
'''
#* import flet as ft: Imports the Flet library, which is used for building GUI applications.
import flet as ft


'''
    Author: Nguyễn Phương Anh Tú
    
    - import pathlib: Imports the pathlib module, which provides an object-oriented interface for working with filesystem paths.
    - BASE_DIR = pathlib.Path(__file__).resolve().parent.parent: Defines BASE_DIR as the parent directory of the current script's parent directory. This is typically used to set a base directory for relative paths in the application.
'''
#* Define directory cho app
import pathlib
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent


'''
    Author: Nguyễn Phương Anh Tú
    
    - PHONE_WIDTH = 400: Sets the base width for the phone UI to 400 pixels.
    - PHONE_HEIGHT = 850: Sets the base height for the phone UI to 850 pixels.
'''
#* Base size of phone
PHONE_WIDTH = 400
PHONE_HEIGHT = 850




'''
    Author: Nguyễn Phương Anh Tú
    
- API_BE = os.getenv('API_BE'): Retrieves the API_BE environment variable from the loaded .env file. This variable typically holds the backend API endpoint.
- DOMAIN_BE = os.getenv('DOMAIN_BE'): Retrieves the DOMAIN_BE environment variable, which likely represents the base domain for the backend.
- DOMAIN_API = f'{DOMAIN_BE}/{API_BE}': Constructs the full API domain URL by combining DOMAIN_BE and API_BE.
- SENTIMENT_API_DOMAIN = os.getenv('SENTIMENT_API_DOMAIN'): Retrieves the SENTIMENT_API_DOMAIN environment variable, which is likely used for sentiment analysis API.
- TURN_ON_SCREEN = os.getenv('TURN_ON_SCREEN') == 'True': Retrieves the TURN_ON_SCREEN environment variable and converts it to a boolean. If the environment variable's value is 'True', TURN_ON_SCREEN will be True; otherwise, it will be False.
'''
#* Load env
from dotenv import load_dotenv # from dotenv import load_dotenv: Imports the load_dotenv function from the dotenv module, which is used to load environment variables from a .env file.
import os
load_dotenv(BASE_DIR / '.env', override=True) # override=True: Overrides existing environment variables if they are already set => auto reload env
API_BE = os.getenv('API_BE')
DOMAIN_BE = os.getenv('DOMAIN_BE')
DOMAIN_API = f'{DOMAIN_BE}/{API_BE}'
SENTIMENT_API_DOMAIN = os.getenv('SENTIMENT_API_DOMAIN')
TURN_ON_SCREEN= os.getenv('TURN_ON_SCREEN')=='True'

