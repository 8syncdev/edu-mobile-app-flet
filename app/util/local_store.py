
import json
from app import (
    BASE_DIR
)

from typing import (
    Literal,
    Optional
)

import os

LocalStoreType = Literal['token']
KEY_TYPE = Literal['access', 'data']


class LocalStore:
    base_dir = BASE_DIR / 'app' / 'data'
    @staticmethod
    def get_data(key:KEY_TYPE, filename: LocalStoreType):
        try:
            with open(LocalStore.base_dir / f'{filename}.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data[key]
        except:
            return None

    @staticmethod
    def set_data(data: dict, filename: LocalStoreType):
        with open(LocalStore.base_dir / f'{filename}.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            
    @staticmethod
    def clear_data(filename: LocalStoreType):
        with open(f'{filename}.json', 'w') as file:
            json.dump({}, file)
            
    @staticmethod
    def clear_all_files():
        for file in os.listdir(LocalStore.base_dir):
            if file.endswith('.json'):
                LocalStore.clear_data(file)