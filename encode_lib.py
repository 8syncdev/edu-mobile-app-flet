'''
    Author: Nguyễn Phương Anh Tú
    ID: 21110105
    Main Purpose:
    => Fix error when reading and rewriting a requirements.txt file with different encodings to package libraries for project dependencies.
'''
import chardet

def read_and_rewrite_requirements(file_path):
    # Detect the encoding
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        print(f"Detected encoding: {encoding}")

    # Read the file with the detected encoding
    with open(file_path, 'r', encoding=encoding, errors='ignore') as file:
        content = file.read()

    # Rewrite the file in UTF-8
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"File {file_path} has been rewritten in UTF-8 encoding.")

# Path to your requirements.txt file
requirements_path = './requirements.txt'
read_and_rewrite_requirements(requirements_path)
