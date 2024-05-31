'''
    Author: Nguyễn Phương Anh Tú
    ID: 21110105
    Main Purpose:
    => Define the main user interface of the application.
'''
from app import (
    ft,  # Import the Flet library
    BASE_DIR,  # Import the base directory constant
    PHONE_HEIGHT,  # Import the phone height constant
    PHONE_WIDTH,  # Import the phone width constant
    TURN_ON_SCREEN  # Import the toggle for screen status
)

from app.style import *  # Import all style constants

from typing import (
    Optional,  # Import Optional type for optional parameters
    Literal,  # Import Literal type for literal type hints
    Dict,  # Import Dict type for dictionary type hints
    Any  # Import Any type for any type hints
)

from app.screens.main_ui.pages.main_page import MainPage  # Import the MainPage class
from app.screens.main_ui.pages.fg_page import FgPage  # Import the FgPage class

from app.schema import (
    TStaticTemplate  # Import the TStaticTemplate type
)

class MainUI(ft.Container):
    '''
        MainUI: A class representing the main user interface of the application.
        Required: user is authenticated
    '''
    def __init__(self, 
                 page: Optional[ft.Page] = None, 
                 static_template: TStaticTemplate = None,
                 **kwargs):
        '''
            Main Purpose:
            => Initialize the MainUI class with the specified parameters.
        '''
        super().__init__(**kwargs)
        self.height = PHONE_HEIGHT  # Set the height of the container
        self.width = PHONE_WIDTH  # Set the width of the container
        self.page = page  # Assign the page parameter to an instance variable
        self.static_template = static_template  # Assign the static_template parameter to an instance variable
        self.bgcolor = BG  # Set the background color
        self.border_radius = 30 if TURN_ON_SCREEN else 0  # Set the border radius based on TURN_ON_SCREEN value
        self.content = ft.Container(  # Create a main container for the UI content
            height=PHONE_HEIGHT,
            width=PHONE_WIDTH,
            content=ft.Stack(  # Use a stack layout for layering UI elements
                controls=[
                    self.init_ui_fgpage(),  # Initialize the foreground page
                    ft.Column(  # Create a column for the main page and bottom navigation bar
                        controls=[
                            ft.Row(  # Create a row for the main page
                                controls=[
                                    self.init_ui_mainpage()  # Initialize the main page
                                ],
                                alignment='end',
                                width=PHONE_WIDTH,
                                height=PHONE_HEIGHT - 60,
                            ),
                            self.init_ui_navbarbottom(),  # Initialize the bottom navigation bar
                        ],
                    )
                ],
                height=PHONE_HEIGHT,
            )
        )

    def init_ui_navbarbottom(self):
        style_navbarbottom = {  # Define styles for the bottom navigation bar icons
            'color': PRIORITY,
            'size': 30,
        }
        self.ui_navbarbottom = ft.Row(  # Create a row for the bottom navigation bar
            controls=[
                ft.Container(  # Create a container for the home icon
                    on_click=lambda e: self.page.go('/'),  # Set the click action to navigate to the home page
                    content=ft.Icon(  # Set the home icon
                        ft.icons.HOME,
                        **style_navbarbottom
                    )
                ),
                ft.Container(  # Create a container for the bookmark icon
                    on_click=lambda e: self.page.go('/course/3?page=1'),  # Set the click action to navigate to the course page
                    content=ft.Icon(
                        ft.icons.BOOKMARK,
                        **style_navbarbottom
                    ),
                ),
                ft.Container(  # Create a container for the support icon
                    on_click=lambda e: self.page.go('/faq'),  # Set the click action to navigate to the FAQ page
                    content=ft.Icon(
                        ft.icons.CONTACT_SUPPORT_OUTLINED,
                        **style_navbarbottom
                    ),
                ),
                ft.Container(  # Create a container for the settings icon
                    on_click=lambda e: self.page.go('/profile'),  # Set the click action to navigate to the profile page
                    content=ft.Icon(
                        ft.icons.SETTINGS,
                        **style_navbarbottom
                    )
                ),
            ],
            width=PHONE_WIDTH,
            alignment='spaceAround',
        )
        return self.ui_navbarbottom  # Return the bottom navigation bar

    def init_ui_navbar(self):
        self.ui_navbar = ft.Row(  # Create a row for the top navigation bar
            controls=[
                ft.Container(  # Create a container for the menu icon
                    on_click=lambda e: self.shrink(e),  # Set the click action to shrink the UI
                    content=ft.Icon(
                        ft.icons.MENU,
                        color=PRIORITY,
                    )
                ),
                ft.Row(  # Create a row for additional icons
                    controls=[
                        ft.Container(  # Create a container for the app icon
                            content=ft.Image(
                                src='/icon.ico',
                                fit=ft.ImageFit.COVER,
                                border_radius=20,
                            ),
                            height=40,
                            width=40,
                            border_radius=20,
                            bgcolor=BG_SEC1,
                            padding=ft.padding.all(2),
                        )
                    ]
                )
            ],
            alignment='spaceBetween',
            height=40,
        )
        return self.ui_navbar  # Return the top navigation bar
    
    def init_ui_fgpage(self):
        self.container_fgpage = FgPage(master=self, page=self.page)  # Initialize the foreground page
        return self.container_fgpage  # Return the foreground page
    
    def init_ui_mainpage(self):
        self.container_mainpage = MainPage(master=self, page=self.page, static_template=self.static_template)  # Initialize the main page
        return self.container_mainpage  # Return the main page
    
    def shrink(self, e):
        self.container_mainpage.width = 120  # Shrink the main page width
        self.container_mainpage.bgcolor = BG_SEC2  # Change the background color
        self.container_mainpage.scale = ft.transform.Scale(  # Scale down the main page
            0.8,
            alignment=ft.alignment.center_right
        )
        self.container_mainpage.border_radius = ft.border_radius.only(  # Adjust the border radius
            top_left=30,
            top_right=0,
            bottom_left=30,
            bottom_right=0
        )
        self.container_mainpage.update()  # Update the main page

    def restore(self, e):
        self.container_mainpage.width = 400  # Restore the main page width
        self.container_mainpage.bgcolor = BG  # Change the background color back
        self.container_mainpage.border_radius = 35  # Adjust the border radius back
        self.container_mainpage.scale = ft.transform.Scale(  # Scale up the main page
            1, alignment=ft.alignment.center_right
        )
        self.container_mainpage.update()  # Update the main page

    def select_route(self):
        route_name = self.page.route  # Get the current route name (incomplete implementation)
