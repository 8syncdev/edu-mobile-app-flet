# Import necessary modules and libraries
from app import (
    ft,  # Importing ft module from the app package
    BASE_DIR,  # Base directory path
    PHONE_HEIGHT,  # Height of the phone screen
    PHONE_WIDTH  # Width of the phone screen
)

from app.style import *  # Importing style settings from the app package

from typing import (  # Importing typing module for type hints
    Optional,
    Literal
)

from app.util import (  # Importing LocalStore module from the app package
    LocalStore
)

from app.hook import (  # Importing AuthHook module from the app package
    AuthHook
)

from app.api import (  # Importing CommonAPI module from the app package
    CommonAPI
)

'''
    Author: Nguyễn Phương Anh Tú
    
    Main Purpose:
    => Define the custom UI components for avatar of the user profile.
'''
# Custom circle UI component
CircleCustom = ft.Stack(
    controls=[
        ft.Container(  # Outer container for the circle
            width=100,  # Width of the circle
            height=100,  # Height of the circle
            border_radius=50,  # Border radius for the circle (making it a circle)
            bgcolor='white12'  # Background color of the circle
        ),
        ft.Container(  # Inner container for the circle (with gradient)
            gradient=ft.SweepGradient(  # Gradient settings
                center=ft.alignment.center,  # Center alignment for the gradient
                start_angle=0.0,  # Start angle of the gradient
                end_angle=3,  # End angle of the gradient
                stops=[0.5, 0.5],  # Gradient stops
                colors=['#00000000', BG_SEC1],  # Gradient colors
            ),
            width=100,  # Width of the inner container
            height=100,  # Height of the inner container
            border_radius=50,  # Border radius for the inner container (making it a circle)
            content=ft.Row(alignment='center',  # Row layout for content alignment
                controls=[
                    ft.Container(  # Container for the circle content
                        padding=ft.padding.all(5),  # Padding around the content
                        bgcolor=BG,  # Background color of the container
                        width=90,  # Width of the container
                        height=90,  # Height of the container
                        border_radius=50,  # Border radius for the container (making it a circle)
                        content=ft.Container(  # Inner container for the circle content
                            bgcolor=FG,  # Background color of the inner container
                            height=80,  # Height of the inner container
                            width=80,  # Width of the inner container
                            border_radius=40,  # Border radius for the inner container (making it a circle)
                            content=ft.Image(  # Image component for the circle content
                                src='brand/brand-14.png',  # Image source
                                width=80,  # Width of the image
                                height=80,  # Height of the image
                                fit=ft.ImageFit.COVER  # Fit mode for the image
                            ),
                        )
                    )
                ],
            ),
        ),
      
    ]
)

# FgPage class definition for profile page UI component
class FgPage(ft.Container):
    '''
        Author: Nguyễn Phương Anh Tú
        
        Main Purpose:
        => Define the custom UI component for the profile page.
    '''
    def __init__(self, 
                 master: Optional[ft.Container] = None,  # Master container
                 page: Optional[ft.Page] = None,  # Page container
                 **kwargs  # Additional keyword arguments
                ):
        super().__init__(**kwargs)  # Initialize the container
        self.master = master  # Master container reference
        self.page = page  # Page container reference
        self.height = PHONE_HEIGHT  # Set height of the container
        self.width = PHONE_WIDTH  # Set width of the container
        self.bgcolor = BG  # Set background color of the container
        self.border_radius = 30  # Set border radius of the container
        self.padding = ft.padding.only(left=10, top=20, right=140)  # Set padding of the container
        self.animate = ft.animation.Animation(600, ft.AnimationCurve.DECELERATE)  # Animation settings
        self.animate_scale = ft.animation.Animation(400, ft.AnimationCurve.DECELERATE)  # Scale animation settings

        self.size_fgpage = PHONE_WIDTH - 140  # Set size of the profile page
        self.content = ft.Column(  # Main content column
            controls=[
                self.init_ui_backnav(),  # Initialize UI for back navigation
                self.init_ui_userinfo(),  # Initialize UI for user information
            ]
        )

    def restore(self, e):  # Method to restore UI
        self.master.restore(e)

    def init_ui_backnav(self):  # Method to initialize UI for back navigation
        '''
            
            
        '''
        self.ui_backnav = ft.Row(  # Row layout for back navigation
            controls=[
                ft.Container(  # Container for back button
                    border_radius=25,  # Border radius for the container
                    padding=ft.padding.only(top=8, left=13),  # Padding for the container
                    height=50,  # Height of the container
                    width=50,  # Width of the container
                    border=ft.border.all(color='white', width=1),  # Border settings for the container
                    on_click=lambda e: self.restore(e),  # Click event handler for restoring
                    content=ft.Text('<', size=20, color=PRIORITY)  # Text content for the back button
                )
            ],
            alignment='end'  # Alignment settings for the row
        )

        return self.ui_backnav  # Return the back navigation UI

    def init_ui_userinfo(self):  # Method to initialize UI for user information
        '''
            Author: Nguyễn Phương Anh Tú
            
        '''
        style_button_nav = {  # Style settings for navigation buttons
            'color': PRIORITY,  # Text color
            'bgcolor': BG,  # Background color
            'on_hover': self.on_hover_btnmenubar,  # Hover event handler
            'width': 160,  # Width of the buttons
            'height': 35,  # Height of the buttons
        }

        # User information column
        self.ui_userinfo = ft.Column(
            controls=[
                CircleCustom,  # Custom circle UI component
                ft.Text(  # Text component for user greeting
                    value="Chào mừng bạn quay trở lại, " + AuthHook.get_user()['username'],  # Greeting message
                    size=20,  # Font size
                    color=PRIORITY,  # Text color
                ),
                ft.Column(  # Column layout for navigation buttons
                    controls=[
                        ft.Column(  # Column layout for primary navigation buttons
                            controls=[
                                ft.ElevatedButton(  # Button for home page navigation
                                    text="Trang chủ",  # Button text
                                    icon=ft.icons.HOME,  # Button icon
                                    **style_button_nav,  # Style settings
                                    on_click=lambda e: self.page.go('/')  # Click event handler
                                ),
                                ft.ElevatedButton(  # Button for course page navigation
                                    text="Khóa học",  # Button text
                                    icon=ft.icons.BOOKMARK,  # Button icon
                                    **style_button_nav,  # Style settings
                                    on_click=lambda e: self.page.go('/course/3?page=1')  # Click event handler
                                ),
                                ft.ElevatedButton(  # Button for contact page navigation
                                    text="Liên hệ",  # Button text
                                    icon=ft.icons.MAIL,  # Button icon
                                    **style_button_nav,  # Style settings
                                    on_click=lambda e: self.page.go('/contact')  # Click event handler
                                ),
                                ft.ElevatedButton(  # Button for bio page navigation
                                    text="Bio",  # Button text
                                    icon=ft.icons.WORK_OUTLINE,  # Button icon
                                    **style_button_nav,  # Style settings
                                    on_click=lambda e: self.page.go('/bio')  # Click event handler
                                ),
                                ft.ElevatedButton(  # Button for dashboard page navigation (for admin)
                                    text="Dashboard",  # Button text
                                    icon=ft.icons.ADMIN_PANEL_SETTINGS,  # Button icon
                                    **style_button_nav,  # Style settings
                                    on_click=lambda e: self.page.go('/dashboard')  # Click event handler
                                ) if CommonAPI.check_admin_role() else ft.Text(''),  # Show only for admin
                            ]
                        ),
                        ft.Column(  # Column layout for secondary navigation buttons
                            controls=[
                                ft.ElevatedButton(  # Button for logout
                                    text="Đăng xuất",  # Button text
                                    icon=ft.icons.LOGOUT,  # Button icon
                                    **style_button_nav,  # Style settings
                                    on_click=lambda e: self.handle_logout(),  # Click event handler
                                ),
                                ft.Container(  # Container for logo image
                                    content=ft.Image(  # Image component
                                        src='admin/admin-logo.png',  # Image source
                                        height=80,  # Height of the image
                                    )
                                ),
                                ft.Row(  # Row layout for social media icons
                                    controls=[
                                        ft.Container(  # Container for GitHub icon
                                            content=ft.Image(  # Image component
                                                src='admin/contact/github.png',  # Image source
                                                height=60  # Height of the image
                                            ),
                                            on_click=lambda e: self.page.launch_url('https://github.com/8syncdev')  # Click event handler
                                        ),
                                        ft.Container(  # Container for TikTok icon
                                            content=ft.Image(  # Image component
                                                src='admin/contact/tiktok.png',  # Image source
                                                height=60  # Height of the image
                                            ),
                                            on_click=lambda e: self.page.launch_url('https://8syncdev.com/bio')  # Click event handler
                                        ),
                                        ft.Container(  # Container for Website icon
                                            content=ft.Image(  # Image component
                                                src='admin/contact/web.png',  # Image source
                                                height=60  # Height of the image
                                            ),
                                            on_click=lambda e: self.page.launch_url('https://8syncdev.com/bio')  # Click event handler
                                        ),
                                    ],
                                    alignment='center',  # Alignment settings for the row
                                )
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Horizontal alignment settings
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Horizontal alignment settings
                    width=self.size_fgpage,  # Width of the column
                    alignment='spaceBetween',  # Alignment settings
                    height=500,  # Height of the column
                )
            ]
        )

        return self.ui_userinfo  # Return the user information UI

    def on_hover_btnmenubar(self, e: ft.HoverEvent):  # Method to handle hover event for navigation buttons
        '''
            Author: Nguyễn Phương Anh Tú
            
        '''
        e.control.bgcolor = BG_SEC1 if e.data == 'true' else BG  # Change background color on hover
        e.control.icon_color = PRIORITY if e.data == 'true' else BG_SEC1  # Change icon color on hover
        # true' else BG_SEC1  # Change icon color on hover based on condition
        e.control.update()  # Update the control

    def handle_logout(self):  # Method to handle logout
        '''
            Author: Nguyễn Phương Anh Tú
            
        '''
        LocalStore.clear_all_files()  # Clear all stored files
        self.page.go('/sign-in')  # Redirect to sign-in page


