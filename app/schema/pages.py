'''
    
    
'''
from typing import Optional, Literal

# Define a type for static template routing
TStaticTemplate = Optional[Literal[
    'intro', 
    'contact', 
    'bio',
    'dashboard',
    'faq',
    'profile',
]]
