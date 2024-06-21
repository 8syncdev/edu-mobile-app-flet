'''
    Author: Nguyễn Phương Anh Tú
    
    Co-op with: Đinh Thành Đức
    
    Main Purpose:
    => The main purpose of this code is to create a local storage system that can read, write, and clear JSON data files. This is useful for persisting data such as tokens or configuration settings locally on the filesystem.
'''
import json
from app import (
    BASE_DIR
)

from typing import (
    Literal,
    Optional
)

import os

# Define type aliases for clarity
LocalStoreType = Literal['token']  # Type alias for specifying the filename type
KEY_TYPE = Literal['access', 'data']  # Type alias for specifying the key type within JSON files

class LocalStore:
    # Set the base directory for storing JSON files
    base_dir = BASE_DIR / 'app' / 'data'
    
    @staticmethod
    def get_data(key:KEY_TYPE, filename: LocalStoreType):
        try:
            # Attempt to open the JSON file and read the data
            with open(LocalStore.base_dir / f'{filename}.json', 'r', encoding='utf-8') as file:
                data = json.load(file)  # Load the JSON data
                return data[key]  # Return the value associated with the specified key
        except:
            return None  # Return None if any error occurs (e.g., file or key not found)

    @staticmethod
    def set_data(data: dict, filename: LocalStoreType):
        # Write the given data to the JSON file, creating or overwriting the file
        with open(LocalStore.base_dir / f'{filename}.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)  # Serialize data to JSON with formatting

    @staticmethod
    def clear_data(filename: LocalStoreType):
        # Clear the JSON file by writing an empty dictionary to it
        with open(f'{filename}', 'w', encoding='utf-8') as file:
            json.dump({}, file, ensure_ascii=False, indent=4)  # Write an empty dictionary to the file

    @staticmethod
    def clear_all_files():
        # Clear all JSON files in the base directory
        for file in os.listdir(LocalStore.base_dir):
            if file.endswith('.json'):
                # Clear the data in each JSON file
                LocalStore.clear_data(LocalStore.base_dir / file)