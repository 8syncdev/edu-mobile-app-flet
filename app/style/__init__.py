'''
    Author: Đinh Thành Đức
    
    Main Purpose:
    => Define the style of the application.
'''


'''
    - Base Style: The base style of the application.
    - PRIORITY: The priority color of the application.
    - MUTED: The muted color of the application.
    - FG: The foreground color of the application.
    - WRAPPER: The wrapper color of the application.
    - BG: The background color of the application.
    - BG_SEC1: The secondary background color of the application.
    - BG_SEC2: The secondary background color of the application.
'''
#* Base Style
PRIORITY = '#fafaf9'
MUTED = '#9e9894'
FG='#292524'
WRAPPER = '#0c0a09'
BG='#09090b'
BG_SEC1 = '#f97316'
BG_SEC2 = '#ea580c'


'''
    - TextCustom: A custom component for text styling.
'''
#* Custom Component
from app.style.custom.TextCustom import TextCustom