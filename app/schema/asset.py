'''
Author: Nguyễn Phương Anh Tú

'''
from typing import (
    Literal
)

# Define literal types for brand and tech keys
KEY_BRAND_TYPE = Literal[
    'brand-1', 'brand-10', 'brand-11', 'brand-12', 'brand-13', 'brand-14', 
    'brand-15', 'brand-2', 'brand-3', 'brand-4', 'brand-5', 'brand-6', 
    'brand-7', 'brand-8', 'brand-9'
]

KEY_TECH_TYPE = Literal[
    'amazonwebservices-plain-wordmark', 'anaconda-original-wordmark', 
    'android-original', 'androidstudio-original', 'angularjs-original', 
    'bootstrap-original-wordmark', 'bootstrap-original', 'c-original', 
    'cplusplus-original', 'csharp-original', 'css3-original', 'devicon-plain', 
    'django-plain-wordmark', 'django-plain', 'docker-original', 'docker-plain-wordmark', 
    'dotnetcore-original', 'dotnetcore-plain', 'fastapi-original-wordmark', 
    'fastapi-original', 'fastapi_icon', 'flutter-original', 'flutter-plain', 
    'gcc-original', 'git-original-wordmark', 'git-original', 'github-original-wordmark', 
    'github-original', 'gitlab-original-wordmark', 'gitlab-original', 'go-original-wordmark', 
    'google-original-wordmark', 'google-original', 'googlecloud-original-wordmark', 
    'html5-original-wordmark', 'html5-plain-wordmark', 'java-original-wordmark', 
    'java-original', 'javascript-original', 'jetbrains-original', 'jquery-original-wordmark', 
    'jquery-original', 'jupyter-original', 'markdown-original', 'materialui-original', 
    'materialui-plain', 'microsoftsqlserver-plain-wordmark', 'microsoftsqlserver-plain', 
    'mongodb-original-wordmark', 'mongodb-original', 'mongodb-plain-wordmark', 
    'mysql-original-wordmark', 'mysql-original', 'nestjs-plain-wordmark', 'nestjs-plain', 
    'nextjs-line', 'nextjs-original-wordmark', 'nextjs-original', 'postgresql-original-wordmark', 
    'postgresql-original', 'pytest-original-wordmark', 'pytest-original', 
    'python-original-wordmark', 'python-original', 'pytorch-original-wordmark', 
    'pytorch-original', 'react-original-wordmark', 'react-original', 'redis-original-wordmark', 
    'redis-original', 'redux-original', 'sass-original', 'sdl-original', 'sdl-plain', 
    'sequelize-original-wordmark', 'sequelize-original', 'spring-original-wordmark', 
    'spring-original', 'sqlite-original-wordmark', 'sqlite-original', 
    'tailwindcss-original-wordmark', 'tailwindcss-plain', 'tomcat-original-wordmark', 
    'tomcat-original', 'typescript-original', 'typescript-plain', 'visualstudio-plain-wordmark', 
    'visualstudio-plain', 'vscode-original-wordmark', 'vscode-original', 'vuejs-original-wordmark', 
    'vuejs-original'
]


def get_brand_imagpath(key: KEY_BRAND_TYPE) -> str:
    """
    Returns the image path for a given brand key.
    """
    return f"brand/{key}.png"


def get_tech_imagpath(key: KEY_TECH_TYPE) -> str:
    """
    Returns the image path for a given tech key.
    """
    return f"tech/{key}.png"


def get_with_relativename(name: str) -> str:
    """
    Returns the image path based on the provided name.
    """
    if 'next' in name.lower():
        return get_tech_imagpath('nextjs-original-wordmark')
    elif 'django' in name.lower():
        return get_tech_imagpath('django-plain-wordmark')
    elif 'python' in name.lower():
        return get_tech_imagpath('python-original-wordmark')
    elif 'c++' in name.lower():
        return get_tech_imagpath('cplusplus-original')
    elif 'java' in name.lower():
        return get_tech_imagpath('java-original-wordmark')
    elif 'go' in name.lower():
        return get_tech_imagpath('go-original-wordmark')
    elif 'react' in name.lower():
        return get_tech_imagpath('react-original-wordmark')
    elif 'fast' in name.lower():
        return get_tech_imagpath('fastapi-original-wordmark')
    
    return get_tech_imagpath('devicon-plain')
